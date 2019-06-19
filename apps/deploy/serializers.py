__author__ = 'singo'
__datetime__ = '2019/4/26 4:27 PM '

from rest_framework import serializers
from .models import Project, DeploymentOrder, History, DeployEnv, EnvServersMap
from common.apis import dingtalk_chatbot
from .common import D_PENDING, D_REJECTED
from common.utils import Bcolor

class ProjectSerializer(serializers.ModelSerializer):
    """
    项目配置序列化类
    """

    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ['id', 'creator']


    def to_representation(self, instance):
        ret = super(ProjectSerializer, self).to_representation(instance)
        ret['creator'] = {
                               'id': instance.creator.id,
                               'name': instance.creator.name
                           }
        # ret['servers']= [{'id': s.id, 'hostname':s.hostname, 'ip':s._IP, 'env': s.env}for s in instance.servers.all()]

        data = []
        for env_server_map in instance.project_maps.all():
            d = {
                'id': env_server_map.id,
                'name': env_server_map.name,
                'parent_ent': env_server_map.parent_env.name if env_server_map.parent_env else None,
                'sub_env': env_server_map.sub_env.name if env_server_map.sub_env else None,
                'servers': [{'id': s.id, 'hostname': s.hostname, 'saltID':s.saltID, 'ip': s._IP, 'env': s.env} for s in
                            env_server_map.servers.all()]
            }
            data.append(d)
        ret['project_maps'] = data
        return ret


class DeploymentOrderSerializer(serializers.ModelSerializer):
    applicant = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = DeploymentOrder
        fields = '__all__'
        read_only_fields = ['id', 'applicant']


    def create(self, validated_data):
        ret = super(DeploymentOrderSerializer, self).create(validated_data)
        # 工单创建审核提醒
        dingtalk_chatbot.text_msg('{}发起了上线申请'.format(ret.applicant.name), at_mobiles=[ret.reviewer.phone])
        return ret

    def update(self, instance, validated_data):
        status = validated_data.get('status', instance.status)
        # 审核状态变更提醒
        if instance.status == 0 and (status == D_PENDING or status == D_PENDING):
            dingtalk_chatbot.text_msg('你的上线申请有状态变更', at_mobiles=[instance.applicant.phone])

        validated_data['status'] = status

        return super(DeploymentOrderSerializer, self).update(instance, validated_data)

    def to_representation(self, instance):
        ret = super(DeploymentOrderSerializer, self).to_representation(instance)
        # 申请人
        ret['applicant'] = {
            'id': instance.applicant.id,
            'name': instance.applicant.name
        }
        # 审核人
        ret['reviewer'] = {
            'id': instance.reviewer.id,
            'name': instance.reviewer.name
        }
        # 执行人
        ret['assign_to'] = {
            'id': instance.assign_to.id,
            'name': instance.assign_to.name
        }
        # 关联项目
        ret ['project'] = {
            'id': instance.project.id,
            'name': instance.project.name
        }

        ret['env'] = instance.env.name

        data = []
        for env_server_map in instance.deploy_maps.all():
            d = {
                'id': env_server_map.id,
                'name': env_server_map.name,
                'parent_ent': env_server_map.parent_env.name if env_server_map.parent_env else None,
                'sub_env': env_server_map.sub_env.name if env_server_map.sub_env else None,
                'servers': [{'id': s.id, 'hostname': s.hostname, 'saltID':s.saltID, 'ip': s._IP, 'env': s.env} for s in
                            env_server_map.servers.all()]
            }
            data.append(d)

        ret['deploy_maps'] = data

        return ret

    def validate_deploy_maps(self, data):
        # 根据发布环境过滤出project所拥有的env-servers
        allow_deploy_maps = self.instance.project.project_maps.all().filter(parent_env__code=self.instance.env.code)

        # env = data.get('env')
        # deploy_maps = data.get('deploy_maps')
        # 根据发布环境过滤出project所拥有的env-servers
        # project_maps = data.get('project').project_maps.all().filter(parent_env__code=env.code)

        if not set(data).issubset(set(allow_deploy_maps)):
            raise serializers.ValidationError('部署服务器超出权限范围')

        return data


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'
        read_only_fields = ['id']


class DeployEnvSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeployEnv
        fields = '__all__'
        read_only_fields = ['id']


class EnvServersMapSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        ret = super(EnvServersMapSerializer, self).to_representation(instance)
        ret['parent_env'] = {'id':instance.parent_env.id, 'name': instance.parent_env.name}
        ret['sub_env'] = {'id': instance.sub_env.id, 'name': instance.sub_env.name} if instance.sub_env else None
        ret['servers'] = [{'id': s.id, 'hostname': s.hostname, 'saltID':s.saltID, 'ip': s._IP}
                          for s in instance.servers.all()]
        return ret

    class Meta:
        model = EnvServersMap
        fields = '__all__'
        read_only_fields = ['id']

    def validate(self, data):
        if data.get('sub_env') and (data.get('parent_env').code != data.get('sub_env').parent.code):
            raise serializers.ValidationError('子环境必须是父环境的子集')
        return data

