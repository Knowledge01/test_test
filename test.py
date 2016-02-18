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

def _check_city(self, cr, uid, ids, context=None):
    for phase in self.read(cr, uid, ids, ['price', 'total'], context=context):
        if phase['price'] and phase['total'] and phase['price'] > phase['total']:
            return False
    return True
_constraints = [
    (_check_city, '单价不可大于总价', ['price', 'total']  ),
]

_sql_constraints = [
        ('name_uniq', 'unique(name)', u'该描述已存在!'),
    ]

@api.onchange('place2')
def _onchange_place2(self, cr, uid, ids, place2,context=None):
    p = self.pool.get('city.distance').browse(cr, uid, place2)
    vals = {'name2': p.distance}
    return {'value': vals}

@api.onchange('price,number')
def onchange_price(self, cr, uid, ids,price,number, context=None):
    return {'value':{'total':price*number}}

@api.onchange('name')
def _username(self):
    self.username = self._context.get('username', self.env.user.name)