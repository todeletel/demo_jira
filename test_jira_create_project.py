# -*- coding: utf-8 -*

from init import jira
template = "项目管理".decode('utf-8')
"""
    不同的JIRA版本 创建项目的默认template不同。需要做兼容处理
"""

jira.create_project(key='Work', name=u"工作", template_name=template)

