__author__ = 'singo'
__datetime__ = '2019/2/25 3:33 PM '


from rest_framework import serializers
from .models import WorkOrder
from users.models.user import User



class WorkOrderSerializer(serializers.ModelSerializer):
    """
    工单序列化类
    """
    # 获取当前登陆用户，并将其赋值给数据库中对应的字段
    applicant = serializers.HiddenField(default=serializers.CurrentUserDefault())
    current_processor = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), label='转发给',
        many=False, allow_empty=True, allow_null=True, default=None)

    class Meta:
        model = WorkOrder
        fields = '__all__'
        read_only_fields = ['id']

    def __get_actions(self, instance):
        # close, process, reject, distribution
        actions = []
        user = self.context['request'].user

        if user.is_superuser:
            return ['close', 'process', 'reject', 'distribution']

        # 工单被指派人按钮
        if user == instance.designator:
            if instance.status == 0:
                actions.extend(['process', 'reject', 'distribution'])
            elif instance.status == 1:
                actions.extend(['reject', 'distribution', 'complete'])
        # 当前处理人按钮
        elif user == instance.current_processor:
            if instance.status == 0:
                actions.extend(['process', 'distribution', 'reject'])
            elif instance.status == 1:
                actions.extend(['complete'])

        # 工单申请人的按钮
        elif user == instance.applicant:
            if instance.status == 0 or instance.status == 1:
                actions.append('close')

        return actions


    def create(self, validated_data):
        # 创建时需要将当前处理者设置成工单指派者
        validated_data['current_processor'] = validated_data.get('designator')
        return super(WorkOrderSerializer, self).create(validated_data)

    def to_representation(self, instance):
        ret = super(WorkOrderSerializer, self).to_representation(instance)

        ret['applicant'] = {
                               'id': instance.applicant.id,
                               'name': instance.applicant.name
                           }
        ret['designator'] = {
                               'id': instance.designator.id,
                               'name': instance.designator.name
                           }
        if instance.current_processor:
            ret['current_processor'] = {
                                'id': instance.current_processor.id,
                                'name': instance.current_processor.name
                            }
        if instance.finally_processor:
            ret['finally_processor'] = {
                                'id': instance.finally_processor.id,
                                'name': instance.finally_processor.name
                            }
        ret['actions'] = self.__get_actions(instance)

        return ret
