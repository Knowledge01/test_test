常用属性
# -*- coding: utf-8 -*-
##############################################################################
# Meto
##############################################################################
from openerp import models, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta
from openerp.osv import fields, osv
import openerp.addons.decimal_precision as dp
import time
from openerp.tools.translate import _
import datetime
import simplejson
class driver_member(models.Model):

_name = 'practice.record'

_order = 'date desc' # 按date字段降序排列，默认为升序

copy=False

readonly=True

required=True

default='not_vip'

string='Arrival Date'

_inherit = ['mail.thread']

help="需要勾选此选项，在费用报销明细中才可见."

常用字段类型
_columns = {
    'name': fields.char(string ='描述'),
    'number' : fields.float(string = '数量'),
    'note': fields.text(string = '备注'),
    'regions': fields.many2many('driver.region', 'driver_member_driver_region_regions_rel', 'a_id', 'b_id','区域',required=True),
    'load': fields.many2one('driver.load',string = '载重'),
    'no_meals': fields.boolean(string = "No Meals"),
    'date': fields.date(string = '日期'),
    'image': fields.binary(string = '车辆图片'),
    'time': fields.datetime(string = '创建时间'),
    'description': fields.html(string = '描述'),
    'state': fields.selection([
                ('not_vip', '非会员'),
                ('review', '待审'),
                ('vip', '正式'),
                ('cancel', '取消'),
                ('stop', '停用'),
                ], string='会员状态',default='not_vip'),
           }

默认值
_defaults = {
        'no_meals': False,
        'date_created': fields.date.today,
        'state': 'draft',
        'user_id': lambda obj, cr, uid, context: uid,
        }

