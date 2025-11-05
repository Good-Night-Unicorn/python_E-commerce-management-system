# coding:utf-8
import random
from datetime import datetime
from sqlalchemy import text,TIMESTAMP

from api.models.models import Base_model
from api.exts import db
from sqlalchemy.dialects.mysql import DOUBLE,LONGTEXT
# 个人信息
class yonghu(Base_model):
    __doc__ = u'''yonghu'''
    __tablename__ = 'yonghu'

    __loginUser__='yonghuzhanghao'


    __authTables__={}
    __authPeople__='是'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    yonghuzhanghao=db.Column( db.VARCHAR(255), nullable=False,unique=True,comment='用户账号' )
    mima=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='密码' )
    yonghuxingming=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='用户姓名' )
    xingbie=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='性别' )
    lianxifangshi=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='联系方式' )
    touxiang=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    money=db.Column( db.Float,default=0 ,  nullable=True, unique=False,comment='余额' )

class guanggaoxinxi(Base_model):
    __doc__ = u'''guanggaoxinxi'''
    __tablename__ = 'guanggaoxinxi'



    __authTables__={}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='是'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    biaoti=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='标题' )
    fengmian=db.Column( db.Text,  nullable=True, unique=False,comment='封面' )
    jianjie=db.Column( db.Text,  nullable=True, unique=False,comment='简介' )
    neirong=db.Column( db.Text,  nullable=True, unique=False,comment='内容' )
    faburiqi=db.Column( db.Date,  nullable=True, unique=False,comment='发布日期' )

class shangpinleixing(Base_model):
    __doc__ = u'''shangpinleixing'''
    __tablename__ = 'shangpinleixing'



    __authTables__={}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    shangpinleixing=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='商品类型' )

class shangpinxinxi(Base_model):
    __doc__ = u'''shangpinxinxi'''
    __tablename__ = 'shangpinxinxi'



    __authTables__={}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='是'
    __intelRecom__='用协'
    __browseClick__='是'
    __foreEndListAuth__='否'
    __foreEndList__='是'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    shangpinbianhao=db.Column( db.VARCHAR(255),  nullable=True,unique=True,comment='商品编号' )
    shangpinmingcheng=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='商品名称' )
    shangpinleixing=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='商品类型' )
    tupian=db.Column( db.Text,  nullable=True, unique=False,comment='图片' )
    guige=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='规格' )
    fabushijian=db.Column( db.Date,  nullable=True, unique=False,comment='发布时间' )
    shangpinjieshao=db.Column( db.Text,  nullable=True, unique=False,comment='商品介绍' )
    onelimittimes=db.Column( db.Integer, default=0 ,  nullable=True, unique=False,comment='单限' )
    alllimittimes=db.Column( db.Integer, default=0 ,  nullable=True, unique=False,comment='库存' )
    thumbsupnum=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='赞' )
    crazilynum=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='踩' )
    clicktime=db.Column( db.DateTime,  nullable=True, unique=False,comment='最近点击时间' )
    clicknum=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='点击次数' )
    discussnum=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='评论数' )
    price=db.Column( db.Float, default=0 , nullable=False, unique=False,comment='价格' )
    onshelves=db.Column( db.Integer,default=1 ,  nullable=True, unique=False,comment='是否上架(1:上架，0:下架)' )
    storeupnum=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='收藏数' )

class yijianfankui(Base_model):
    __doc__ = u'''yijianfankui'''
    __tablename__ = 'yijianfankui'



    __authTables__={'yonghuzhanghao':'yonghu',}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    biaoti=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='标题' )
    fengmian=db.Column( db.Text,  nullable=True, unique=False,comment='封面' )
    fankuishijian=db.Column( db.Date,  nullable=True, unique=False,comment='反馈时间' )
    yijianfankui=db.Column( db.Text,  nullable=True, unique=False,comment='意见反馈' )
    yonghuzhanghao=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户账号' )
    yonghuxingming=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户姓名' )
    shhf=db.Column( db.Text,  nullable=True, unique=False,comment='回复内容' )

class forum(Base_model):
    __doc__ = u'''forum'''
    __tablename__ = 'forum'



    __authTables__={}
    __foreEndListAuth__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    title=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='帖子标题' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='帖子内容' )
    parentid=db.Column( db.BigInteger, default=0 ,  nullable=True, unique=False,comment='父节点id' )
    userid=db.Column( db.BigInteger, default=0 , nullable=False, unique=False,comment='用户id' )
    username=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户名' )
    avatarurl=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    isdone=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='状态' )
    istop=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='是否置顶' )
    toptime=db.Column( db.DateTime,  nullable=True, unique=False,comment='置顶时间' )
    typename=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='分类名称' )
    cover=db.Column( db.Text,  nullable=True, unique=False,comment='封面' )
    isanon=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='是否匿名(1:是,0:否)' )
    delflag=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='是否删除(1:是,0:否)' )

class forumtype(Base_model):
    __doc__ = u'''forumtype'''
    __tablename__ = 'forumtype'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    typename=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='分类名称' )

class forumreport(Base_model):
    __doc__ = u'''forumreport'''
    __tablename__ = 'forumreport'



    __authTables__={}
    __authSeparate__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    forumid=db.Column( db.BigInteger, default=0 ,  nullable=True, unique=False,comment='论坛id' )
    title=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='帖子标题' )
    userid=db.Column( db.BigInteger, default=0 , nullable=False, unique=False,comment='举报用户id' )
    username=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='举报用户名' )
    reporteduserid=db.Column( db.BigInteger, default=0 , nullable=False, unique=False,comment='被举报用户id' )
    reportedusername=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='被举报用户名' )
    reason=db.Column( db.Text, nullable=False, unique=False,comment='举报原因' )
    picture=db.Column( db.Text,  nullable=True, unique=False,comment='图片补充' )
    handleadvise=db.Column( db.Text,  nullable=True, unique=False,comment='处理建议' )
    status=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='状态' )
    reporttype=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='举报类型' )

class cart(Base_model):
    __doc__ = u'''cart'''
    __tablename__ = 'cart'



    __authTables__={}
    __authSeparate__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    tablename=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='商品表名' )
    userid=db.Column( db.BigInteger, default=0 , nullable=False, unique=False,comment='用户id' )
    goodid=db.Column( db.BigInteger, default=0 , nullable=False, unique=False,comment='商品id' )
    goodname=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='商品名称' )
    picture=db.Column( db.Text,  nullable=True, unique=False,comment='图片' )
    buynumber=db.Column( db.Integer, default=0 , nullable=False, unique=False,comment='购买数量' )
    price=db.Column( db.Float, default=0 ,  nullable=True, unique=False,comment='单价' )

class orders(Base_model):
    __doc__ = u'''orders'''
    __tablename__ = 'orders'



    __authTables__={}
    __authSeparate__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    orderid=db.Column( db.VARCHAR(255), nullable=False,unique=True,comment='订单编号' )
    tablename=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='商品表名' )
    userid=db.Column( db.BigInteger, default=0 , nullable=False, unique=False,comment='用户id' )
    goodid=db.Column( db.BigInteger, default=0 , nullable=False, unique=False,comment='商品id' )
    goodname=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='商品名称' )
    picture=db.Column( db.Text,  nullable=True, unique=False,comment='商品图片' )
    buynumber=db.Column( db.Integer, default=0 , nullable=False, unique=False,comment='购买数量' )
    price=db.Column( db.Float,default=0 , nullable=False, unique=False,comment='价格' )
    total=db.Column( db.Float,default=0 , nullable=False, unique=False,comment='总价格' )
    type=db.Column( db.Integer,default=1 ,  nullable=True, unique=False,comment='支付类型' )
    status=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='状态' )
    address=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='地址' )
    tel=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='电话' )
    consignee=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='收货人' )
    logistics=db.Column( db.Text,  nullable=True, unique=False,comment='物流' )
    remark=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='备注' )
    sfsh=db.Column( db.VARCHAR(255),default='待审核', nullable=True, unique=False,comment='是否审核' )
    shhf=db.Column( db.Text,  nullable=True, unique=False,comment='审核回复' )
    role=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户角色' )
    returnreason=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='退货原因' )

class address(Base_model):
    __doc__ = u'''address'''
    __tablename__ = 'address'



    __authTables__={}
    __authSeparate__='是'
    __foreEndListAuth__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    userid=db.Column( db.BigInteger, default=0 , nullable=False, unique=False,comment='用户id' )
    address=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='地址' )
    name=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='收货人' )
    phone=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='电话' )
    isdefault=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='是否默认地址[是/否]' )

class chargerecord(Base_model):
    __doc__ = u'''chargerecord'''
    __tablename__ = 'chargerecord'



    __authTables__={}
    __authSeparate__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    userid=db.Column( db.BigInteger, default=0 , nullable=False, unique=False,comment='用户id' )
    username=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='用户名' )
    role=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='角色' )
    amount=db.Column( db.Float, default=0 , nullable=False, unique=False,comment='金额' )

class newstype(Base_model):
    __doc__ = u'''newstype'''
    __tablename__ = 'newstype'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    typename=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='分类名称' )

class news(Base_model):
    __doc__ = u'''news'''
    __tablename__ = 'news'



    __authTables__={}
    __thumbsUp__='是'
    __intelRecom__='是'
    __browseClick__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    title=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='标题' )
    introduction=db.Column( db.Text,  nullable=True, unique=False,comment='简介' )
    typename=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='分类名称' )
    name=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='发布人' )
    headportrait=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    clicknum=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='点击次数' )
    clicktime=db.Column( db.DateTime,  nullable=True, unique=False,comment='最近点击时间' )
    thumbsupnum=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='赞' )
    crazilynum=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='踩' )
    storeupnum=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='收藏数' )
    picture=db.Column( db.Text, nullable=False, unique=False,comment='图片' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='内容' )

class storeup(Base_model):
    __doc__ = u'''storeup'''
    __tablename__ = 'storeup'



    __authTables__={}
    __authSeparate__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    userid=db.Column( db.BigInteger, default=0 , nullable=False, unique=False,comment='用户id' )
    refid=db.Column( db.BigInteger, default=0 ,  nullable=True, unique=False,comment='商品id' )
    tablename=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='表名' )
    name=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='名称' )
    picture=db.Column( db.Text,  nullable=True, unique=False,comment='图片' )
    type=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='类型' )
    inteltype=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='推荐类型' )
    remark=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='备注' )

class discussshangpinxinxi(Base_model):
    __doc__ = u'''discussshangpinxinxi'''
    __tablename__ = 'discussshangpinxinxi'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    refid=db.Column( db.BigInteger, default=0 , nullable=False, unique=False,comment='关联表id' )
    userid=db.Column( db.BigInteger, default=0 , nullable=False, unique=False,comment='用户id' )
    avatarurl=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    nickname=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户名' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='评论内容' )
    reply=db.Column( db.Text,  nullable=True, unique=False,comment='回复内容' )
    thumbsupnum=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='赞' )
    crazilynum=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='踩' )
    istop=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='置顶(1:置顶,0:非置顶)' )
    tuserids=db.Column( db.Text,  nullable=True, unique=False,comment='赞用户ids' )
    cuserids=db.Column( db.Text,  nullable=True, unique=False,comment='踩用户ids' )

