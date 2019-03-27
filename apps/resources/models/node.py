__author__ = 'singo'
__datetime__ = '2019/1/9 2:38 PM '

from django.db import models, transaction
from django.db.transaction import atomic
import uuid

class Node(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    key = models.CharField(unique=True, null=False, blank=False, max_length=64)
    child_mark = models.IntegerField(default=0)
    name = models.CharField(max_length=32, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @classmethod
    def default_node(cls, name='DEFAULT'):
        from django.db.models import Q
        root = cls.objects.filter(key__regex=r'[0-9]+$').filter(Q(name=name))
        if root:
            return root[0]
        else:
            key = str(cls.get_next_root_key())
            return  cls.objects.create(**{'key': key, 'name': name})

    def get_next_child_key(self):
        self.child_mark += 1
        self.save()
        return '{}:{}'.format(self.key, self.child_mark-1)

    @property
    def is_root(self):
        # 如果key是数字说明是根节点
        return self.key.isdigit()

    @classmethod
    def get_next_root_key(cls):
        try:
            node = cls.objects.filter(key__regex=r'^[0-9]+$').latest('created')
            return str((int(node.key) + 1))
        except Node.DoesNotExist:
            return '0'
        # return str((int(node.key)+1)) if node else '0'

    @classmethod
    def get_root_brothers(cls):
        return cls.objects.filter(key__regex=r'^[0-9]+$')

    @property
    def father_key(self):
        return ':'.join(self.key.split(':')[:-1])

    @property
    def father(self):
        '''
        获取父节点,如果是根节点就直接返回, 如果不存着就创建默认节点
        :return:
        '''
        if self.is_root:
            return self
        try:
            return  self.__class__.objects.get(key=self.father_key)
        except Node.DoesNotExist:
            return self.__class__.default_node()

    @father.setter
    def father(self, father):
        children = self.all_children
        old_key = self.key
        self.key = father.get_next_child_key()
        with atomic():
            for child in children:
                child.key = child.key.replace(old_key, self.key, 1)
                child.save()
            self.save()

    @property
    def brothers(self):
        if self.is_root:
            return self.__class__.get_root_brothers()
        else:
            father = self.father
            return  father.children()

    @property
    def children(self):
        pattern = r'^{0}:[0-9]+$'
        return self.__class__.objects.filter(key__regex=pattern.format(self.key))

    @property
    def all_children(self):
        pattern = r'^{0}:'
        return self.__class__.objects.filter(key__regex=pattern.format(self.key))

    def create_child(self, name):
        with transaction.atomic():
            child_key = self.get_next_child_key()
            return self.__class__.objects.create(key=child_key, name=name)
