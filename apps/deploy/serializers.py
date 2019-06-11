__author__ = 'singo'
__datetime__ = '2019/4/26 4:27 PM '

from rest_framework import serializers
from .models import Project, DeploymentOrder, History, DeployEnv, DeployItem
from common.apis import dingtalk_chatbot
from .common import D_PENDING, D_REJECTED


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
        ret['servers']= [{'id': s.id, 'hostname':s.hostname, 'ip':s._IP, 'env': s.env}for s in instance.servers.all()]

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
        instance.status = status
        instance.save()
        return instance

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

        return ret



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


class DeployItemSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        ret = super(DeployItemSerializer, self).to_representation(instance)
        ret['parent_env'] = instance.parent_env.name
        ret['sub_env'] = instance.sub_env.name if instance.sub_env else None
        ret['servers'] = [{'id': s.id, 'hostname': s.hostname, 'ip': s._IP, 'saltID':s.saltID} for s in
                          instance.servers.all()]
        return ret

    class Meta:
        model = DeployItem
        fields = '__all__'
        read_only_fields = ['id']