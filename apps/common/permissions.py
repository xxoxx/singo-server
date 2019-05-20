from rest_framework import permissions
from rest_framework.permissions import BasePermission
from rest_framework import exceptions
from django.core.urlresolvers import resolve

class IsSuperuser(BasePermission):
    """
    Allows access only to superuser users.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_superuser

class IsSuperuserOrSelf(IsSuperuser):

    def has_permission(self, request, view):
        return True

    # 只有在已经通过了视图级别has_permission检查时，
    # 才会调用实例级别的has_object_permission方法。
    # 另请注意，为了运行实例级别检查，视图代码应显式调用.
    # check_object_permissions（request，obj）
    # 如果您使用的是通用视图，则默认情况下将为您处理。
    # （基于函数的视图需要显式检查对象权限，在失败时引发

    def has_object_permission(self, request, view, obj):
        return super(IsSuperuserOrSelf, self).has_permission(request, view) or request.user.is_owner(obj)


# 自定义权限
class DevopsPermission(permissions.BasePermission):
    def get_required_permissions(self, method, app_label, perms_map):
        if method not in perms_map:
            raise exceptions.MethodNotAllowed(method)
        return [perm.format(app_label) for perm in perms_map[method]]

    def has_permission(self, request, view):
        if request.user and request.user.is_superuser:
            return True
        app_label = resolve(request.path).app_name
        perms = self.get_required_permissions(request.method, app_label, view.perms_map)
        return request.user.has_perms(perms)

# 发布权限
class DeployPermission(permissions.BasePermission):
    message = '你没有执行发布的权限'

    # 超级用户、运维、执行人拥有此权限
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or request.user.is_devops or (obj.assign_to == request.user)

# 是运维返回True
class IsDevopsPermission(permissions.BasePermission):
    message = '只要运维人员才拥有此权限'
    def has_permission(self, request, view):
        return request.user.is_devops or request.user.is_superuser