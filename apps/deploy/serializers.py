__author__ = 'singo'
__datetime__ = '2019/4/26 4:27 PM '

from rest_framework import serializers
from .models import Project, DeploymentOrder, History


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
        ret['servers']= [{'id': s.id, 'hostname':s.hostname, 'ip':s._IP}for s in instance.servers.all()]

        return ret

class DeploymentOrderSerializer(serializers.ModelSerializer):
    applicant = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = DeploymentOrder
        fields = '__all__'
        read_only_fields = ['id', 'applicant']

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

        return ret

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'
        read_only_fields = ['id']