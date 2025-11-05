<template>
	<div class="center-preview">
		<div class="center-title">{{ title }}</div>
		<div class="center-info">
			<div class="center-info-title">个人信息</div>
			<div class="img-box" v-if="userTableName=='yonghu'">
				<img :src="sessionForm.touxiang?baseUrl + sessionForm.touxiang:require('@/assets/avator.png')">
			</div>
			<div class="info-item1" v-if="userTableName=='yonghu'">
				<span class="icon iconfont icon-shouye-zhihui"></span>
				<div class="label">用户账号：</div>
				<div class="text">{{sessionForm.yonghuzhanghao}}</div>
			</div>
			<div class="info-item2" v-if="userTableName=='yonghu'">
				<span class="icon iconfont icon-shouye-zhihui"></span>
				<div class="label">用户姓名：</div>
				<div class="text">{{sessionForm.yonghuxingming}}</div>
			</div>
			<div class="info-item3" v-if="userTableName=='yonghu'">
				<span class="icon iconfont icon-shouye-zhihui"></span>
				<div class="label">性别：</div>
				<div class="text">{{sessionForm.xingbie}}</div>
			</div>
			<div class="info-item4" v-if="userTableName=='yonghu'">
				<span class="icon iconfont icon-shouye-zhihui"></span>
				<div class="label">联系方式：</div>
				<div class="text">{{sessionForm.lianxifangshi}}</div>
			</div>
			<div class="info-item5" v-if="userTableName=='yonghu'">
				<span class="icon iconfont icon-shouye-zhihui"></span>
				<div class="label">余额：</div>
				<div class="text">{{sessionForm.money}}</div>
			</div>
		
		</div>
	
		<el-tabs class="center-tabs" tab-position="left" @tab-click="handleClick">
			<el-tab-pane label="个人中心">
				<el-form class="center-preview-pv" ref="sessionForm" :model="sessionForm" :rules="rules" label-width="180px">
					<el-form-item class="center-item" v-if="userTableName=='yonghu'" label="用户账号" prop="yonghuzhanghao">
						<el-input v-model="sessionForm.yonghuzhanghao" placeholder="用户账号" readonly></el-input>
					</el-form-item>
					<el-form-item class="center-item" v-if="userTableName=='yonghu'" label="用户姓名" prop="yonghuxingming">
						<el-input v-model="sessionForm.yonghuxingming" placeholder="用户姓名" ></el-input>
					</el-form-item>
					<el-form-item class="center-item" v-if="userTableName=='yonghu'" label="性别" prop="xingbie">
						<el-select v-model="sessionForm.xingbie" placeholder="请选择性别" >
							<el-option v-for="(item, index) in dynamicProp.xingbie" :key="index" :label="item" :value="item"></el-option>
						</el-select>
					</el-form-item>
					<el-form-item class="center-item" v-if="userTableName=='yonghu'" label="联系方式" prop="lianxifangshi">
						<el-input v-model="sessionForm.lianxifangshi" placeholder="联系方式" ></el-input>
					</el-form-item>
					<el-form-item class="center-item" v-if="userTableName=='yonghu'" label="头像" prop="touxiang">
						<file-upload
							tip="点击上传头像"
							action="file/upload"
							:limit="1"
							:multiple="true"
							:fileUrls="sessionForm.touxiang?sessionForm.touxiang:''"
							@change="yonghutouxiangHandleAvatarSuccess"
							></file-upload>
					</el-form-item>
					<el-form-item class="center-item" v-if="userTableName=='yonghu'" label="余额">
						<div class="balance-item">
							<el-input v-model="sessionForm.money" placeholder="余额" readonly></el-input>
							<div class="balanceBtn" @click="dialogFormVisibleMoney = true">
								<span class="icon iconfont icon-tijiaoyanzi"></span>
								<span class="text">点我充值</span>
							</div>
						</div>
					</el-form-item>
					<el-form-item class="center-btn-item">
						<div class="updateBtn" type="primary" @click="onSubmit('sessionForm')">
							<span class="icon iconfont icon-kaitongfuwu"></span>
							<span class="text">提交</span>
						</div>
						<div class="closeBtn" type="danger" @click="logout">
							<span class="icon iconfont icon-shanchu1"></span>
							<span class="text">退出登录</span>
						</div>
					</el-form-item>
				</el-form>
			</el-tab-pane>
			<el-tab-pane label="修改密码">
				<el-form class="center-preview-pv" ref="passwordForm" :model="passwordForm" :rules="passwordRules" label-width="180px">
					<el-form-item class="center-item" label="原密码" prop="password">
						<el-input type="password" v-model="passwordForm.password" placeholder="原密码"></el-input>
					</el-form-item>
					<el-form-item class="center-item" label="新密码" prop="newpassword">
						<el-input type="password" v-model="passwordForm.newpassword" placeholder="新密码"></el-input>
					</el-form-item>
					<el-form-item class="center-item" label="确认密码" prop="repassword">
						<el-input type="password" v-model="passwordForm.repassword" placeholder="确认密码"></el-input>
					</el-form-item>
					<el-form-item class="center-btn-item">
						<div class="updateBtn" type="primary" @click="updatePassword">
							<span class="icon iconfont icon-kaitongfuwu"></span>
							<span class="text">修改密码</span>
						</div>
					</el-form-item>
				</el-form>
			</el-tab-pane>
			<el-tab-pane v-for="(item,index) in menuList" :key="index" v-if="hasBack(item.menu)" :label="item.child[0].menu" :name="item.child[0].tableName"></el-tab-pane>
			<el-tab-pane label="我的发布"></el-tab-pane>
			<el-tab-pane label="我的订单"></el-tab-pane>
			<el-tab-pane label="我的地址" name="MyAddress">
				<router-view></router-view>
			</el-tab-pane>
			<el-tab-pane label="我的收藏"></el-tab-pane>
		</el-tabs>

		<el-dialog title="用户充值" :visible.sync="dialogFormVisibleMoney" width="726px" center>
			<el-form :model="chongzhiForm">
				<el-form-item label="充值金额" label-width="120px">
					<el-input type="number" v-model="chongzhiForm.money" autocomplete="off" placeholder="充值金额"></el-input>
				</el-form-item>
				<el-form-item label-width="120px">
					<el-radio-group v-model="chongzhiForm.radio">
						<el-radio style="margin-bottom: 30px" label="微信支付">
							<el-image
								style="width: 60px; height: 60px;vertical-align: middle;"
								:src="require('@/assets/weixin.png')"
								fit="fill"></el-image>
							<span style="display: inline-block;margin-left: 10px">微信支付</span>
						</el-radio>
						<el-radio label="支付宝支付">
							<el-image
								style="width: 60px; height: 60px;vertical-align: middle;"
								:src="require('@/assets/zhifubao.png')"
								fit="fill"></el-image>
							<span style="display: inline-block;margin-left: 10px">支付宝支付</span>
						</el-radio>
						<el-radio label="中国建设银行支付">
							<el-image
								style="width: 120px; height: 60px;vertical-align: middle;"
								:src="require('@/assets/jianshe.png')"
								fit="fill"></el-image>
						</el-radio>
						<el-radio label="中国农业银行支付">
							<el-image
								style="width: 126px; height: 60px;vertical-align: middle;"
								:src="require('@/assets/nongye.png')"
								fit="fill"></el-image>
						</el-radio>
						<el-radio label="中国银行支付">
							<el-image
								style="width: 140px; height: 60px;vertical-align: middle;"
								:src="require('@/assets/zhongguo.png')"
								fit="fill"></el-image>
						</el-radio>
						<el-radio label="交通银行支付">
							<el-image
								style="width: 120px; height: 60px;vertical-align: middle;"
								:src="require('@/assets/jiaotong.png')"
								fit="fill"></el-image>
						</el-radio>
					</el-radio-group>
				</el-form-item>
			</el-form>
			<div slot="footer" class="dialog-footer">
				<el-button @click="dialogFormVisibleMoney = false">取 消</el-button>
				<el-button type="primary" @click="chongzhi">确认充值</el-button>
			</div>
		</el-dialog>
	</div>
</template>

<script>
	import config from '@/config/config';
	import menu from '@/config/menu';
	import Vue from 'vue';
	export default {
		//数据集合
		data() {
			return {
				title: '个人中心',
				baseUrl: config.baseUrl,
				sessionForm: {},
				passwordForm: {},
				passwordRules: {
					password: [
						{
							required: true,
							message: "密码不能为空",
							trigger: "blur"
						}
					],
					newpassword: [
						{
							required: true,
							message: "新密码不能为空",
							trigger: "blur"
						}
					],
					repassword: [
						{
							required: true,
							message: "确认密码不能为空",
							trigger: "blur"
						}
					]
				},
				rules: {},
				chongzhiForm: {
					money: '',
					radio: ''
				},
				menuList: [],
				disabled: false,
				dialogFormVisibleMoney: false,
				uploadUrl: config.baseUrl + 'file/upload',
				imageUrl: '',
				headers: {Token: localStorage.getItem('frontToken')},
				userTableName: localStorage.getItem('UserTableName'),
				dynamicProp: {},
			}
		},
		created() {
			let menus = menu.list()
			for(let x in menus){
				if(menus[x].tableName == this.userTableName){
					for(let i in menus[x].backMenu){
						if(menus[x].backMenu[i].menu=='考试管理'){
							menus[x].backMenu.splice(i,1)
						}
					}
					this.menuList = menus[x].backMenu
				}
			}
			if ('yonghu' == this.userTableName) {
				this.$set(this.sessionForm, 'yonghuzhanghao', null);
			}
			if ('yonghu' == this.userTableName) {
				this.$set(this.sessionForm, 'mima', null);
			}
			if ('yonghu' == this.userTableName) {
				this.$set(this.sessionForm, 'yonghuxingming', null);
			}
			if ('yonghu' == this.userTableName) {
				this.$set(this.sessionForm, 'xingbie', null);
			}
			if ('yonghu' == this.userTableName) {
				this.$set(this.sessionForm, 'lianxifangshi', null);
			}
			if ('yonghu' == this.userTableName) {
				this.$set(this.sessionForm, 'touxiang', null);
			}
			if ('yonghu' == this.userTableName) {
				this.$set(this.sessionForm, 'money', null);
			}

			if ('yonghu' == this.userTableName&&this.rules['yonghuzhanghao']){
				this.rules['yonghuzhanghao'].push({ required: true, message: '请输入用户账号', trigger: 'blur' })
			}else if('yonghu' == this.userTableName&&!this.rules['yonghuzhanghao']) {
				this.$set(this.rules, 'yonghuzhanghao', [{ required: true, message: '请输入用户账号', trigger: 'blur' }]);
			}
			if ('yonghu' == this.userTableName&&this.rules['mima']){
				this.rules['mima'].push({ required: true, message: '请输入密码', trigger: 'blur' })
			}else if('yonghu' == this.userTableName&&!this.rules['mima']) {
				this.$set(this.rules, 'mima', [{ required: true, message: '请输入密码', trigger: 'blur' }]);
			}
			if ('yonghu' == this.userTableName&&this.rules['yonghuxingming']){
				this.rules['yonghuxingming'].push({ required: true, message: '请输入用户姓名', trigger: 'blur' })
			}else if('yonghu' == this.userTableName&&!this.rules['yonghuxingming']) {
				this.$set(this.rules, 'yonghuxingming', [{ required: true, message: '请输入用户姓名', trigger: 'blur' }]);
			}
			if ('yonghu' == this.userTableName) {
				this.$set(this.rules, 'lianxifangshi', [{ required: false, validator: this.$validate.isMobile, trigger: 'blur' }]);
			}
			if ('yonghu' == this.userTableName) {
				this.$set(this.rules, 'money', [{ required: false, validator: this.$validate.isNumber, trigger: 'blur' }]);
			}

			this.init();
			this.sessionForm = JSON.parse(localStorage.getItem('sessionForm'))
		},
		//方法集合
		methods: {
			init() {
				if ('yonghu' == this.userTableName) {
					this.dynamicProp.xingbie = '男,女'.split(',');
				}
			},
			setSession(){
				localStorage.setItem('sessionForm',JSON.stringify(this.sessionForm))
			},
			onSubmit(formName) {
				if(`yonghu` == this.userTableName && this.sessionForm.touxiang!=null){
					this.sessionForm.touxiang = this.sessionForm.touxiang.replace(new RegExp(this.$config.baseUrl,"g"),"");
				}
				this.$refs[formName].validate((valid) => {
					if (valid) {
						this.$http.post(this.userTableName + '/update', this.sessionForm).then(res => {
							if (res.data.code == 0) {
								this.setSession()
								this.$message({
									message: '更新成功',
									type: 'success',
									duration: 1500
								});
							}
						});
					} else {
						return false;
					}
				});
			},
			yonghutouxiangHandleAvatarSuccess(fileUrls) {
				this.sessionForm.touxiang = fileUrls;
			},
			chongzhi() {
				if (this.chongzhiForm.money == '') {
					this.$message({
						message: '请输入充值金额',
						type: 'error',
						duration: 1500
					});
					return;
				}
				if (this.chongzhiForm.money <= 0) {
					this.$message({
						message: '请输入正确的充值金额',
						type: 'error',
						duration: 1500
					});
					return;
				}
				if (this.chongzhiForm.radio == '') {
					this.$message({
						message: '请选择充值方式',
						type: 'error',
						duration: 1500
					});
					return;
				}
				if(!this.sessionForm.money) {
					this.sessionForm.money = parseFloat(this.chongzhiForm.money)
				}else{
					this.sessionForm.money = parseFloat(this.sessionForm.money) + parseFloat(this.chongzhiForm.money);
				}
				
				this.$http.post(this.userTableName + '/update', this.sessionForm).then(res => {
					if (res.data.code == 0) {
						this.$http.post('chargerecord/add',{
							username: localStorage.getItem("username"),
							role: localStorage.getItem("frontRole"),
							amount: parseFloat(this.chongzhiForm.money),
							userid: this.sessionForm.id
						}).then(rs=>{
							this.setSession()
							this.$message({
								message: '充值成功',
								type: 'success',
								duration: 1500,
								onClose: () => {
									this.dialogFormVisibleMoney = false;
								}
							});
						})
					}
				});
			},
			handleClick(tab, event) {
				switch(event.target.outerText) {
					case '个人中心':
						tab.$router.push('/index/center');
						break;
					case '修改密码':
						this.passwordForm = {
							password: '',
							newpassword: '',
							repassword: '',
						}
						this.$forceUpdate()
						break;
					case '我的发布':
						tab.$router.push('/index/myForumList');
						break;
					case '我的订单':
						tab.$router.push('/index/shop-order/order');
						break;
					case '我的地址':
						tab.$router.push('/index/shop-address/list');
						break;
					case '我的收藏':
						localStorage.setItem('storeupType', 1);
						tab.$router.push('/index/storeup');
						break;
					default:
						tab.$router.push(`/index/${tab.name}?centerType=1`);
				}

				this.title = event.target.outerText;
			},
			async updatePassword(){
				this.$refs["passwordForm"].validate(async valid => {
					if (valid) {
						var password = "";
						if (this.sessionForm.mima) {
							password = this.sessionForm.mima;
						} else if (this.sessionForm.password) {
							password = this.sessionForm.password;
						}
						if (this.userTableName == 'yonghu') {
						}
						if (this.passwordForm.password != password) {
							this.$message.error("原密码错误");
							return;
						}
						if (this.passwordForm.newpassword != this.passwordForm.repassword) {
							this.$message.error("两次密码输入不一致");
							return;
						}
						if (this.passwordForm.newpassword == this.passwordForm.password) {
							this.$message.error("新密码与原密码相同！");
							return;
						}
						this.sessionForm.password = this.passwordForm.newpassword;
						this.sessionForm.mima = this.passwordForm.newpassword;
						this.$http.post(`${this.userTableName}/update`,this.sessionForm).then(({data})=>{
							if (data && data.code === 0) {
								this.$message({
									message: "修改密码成功,下次登录系统生效",
									type: "success",
									duration: 1500,
									onClose: () => {
									}
								});
								this.setSession()
							} else {
								this.$message.error(data.msg);
							}
						});
					}
				})
			},
			logout() {
				localStorage.clear();
				Vue.http.headers.common['Token'] = "";
				this.$router.push('/index/home');
				this.activeIndex = '0'
				localStorage.setItem('keyPath', this.activeIndex)
				this.$forceUpdate()
				this.$message({
					message: '登出成功',
					type: 'success',
					duration: 1500,
				});
			},
			hasBack(name){
				switch(name){
					case '订单管理':
						return false
						break;
					case '我的收藏管理':
						return false
						break;
					default:
						return true
				}
			}
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.center-preview {
		padding: 30px calc((100% - 1200px)/2);
		margin: 0px auto;
		background: #EDF0FA;
		width: 100%;
		position: relative;
		.center-title {
			padding: 0  165px;
			margin: 0;
			flex-direction: column;
			color: #44446D;
			background: url(http://codegen.caihongy.cn/20250118/8fc0638edcbd47b4bdaa28e8495ba36b.png) no-repeat center center / 100% 100%;
			display: flex;
			width: 100%;
			font-size: 32px;
			line-height: 100px;
			justify-content: flex-end;
			text-align: left;
			height: 100px;
		}
		.center-info {
			border-radius: 0;
			padding: 120px 20px 100px 185px;
			box-shadow: 0 0px 0px rgba(0, 0, 0, 0.3);
			margin: 0px auto;
			background: url(http://codegen.caihongy.cn/20250204/f807d28c2d19470385fc106b199d9978.png) no-repeat  center center / 100% 100%;
			display: inline-block;
			width: 100%;
			min-height: 300px;
			position: relative;
			height: auto;
			.center-info-title {
				border-radius: 30px;
				z-index: 1;
				color: #333;
				top: 20px;
				left: 165px;
				background: #44446D80;
				display: flex;
				width: calc(100% - 412px);
				font-size: 0;
				line-height: 1;
				position: absolute;
				height: calc(100% - 40px);
			}
			.img-box {
				border-radius:  45px;
				z-index: 1;
				top: 21px;
				width: 200px;
				font-size: 0;
				border-color: #efefef;
				border-width: 0;
				position: absolute;
				right: 20px;
				border-style: solid;
				height: calc(100% - 60px);
				img {
					border-radius:  45px;
					margin: 20px auto;
					object-fit: cover;
					display: block;
					width: 100px;
					border-color: #efefef;
					border-width: 0 0 1px 0;
					border-style: solid;
					height: 100px;
				}
			}
			.info-item1 {
				padding: 0 0px;
				z-index: 1;
				bottom: 90px;
				display: flex;
				width: auto;
				line-height: 1;
				justify-content: center;
				align-items: flex-end;
				position: absolute;
				right: 60px;
				height: auto;
				.icon {
					padding: 0 5px;
					color: #333;
					display: none;
					font-size: 14px;
				}
				.label {
					padding: 0 5px 0 0;
					color: #FFFFFF;
					white-space: nowrap;
					font-size: 16px;
					line-height: 1;
				}
				.text {
					color: #FFFFFF;
					white-space: nowrap;
					font-size: 16px;
					line-height: 1;
					text-align: right;
				}
			}
			.info-item2 {
				padding: 0 20px;
				z-index: 1;
				display: inline-block;
				width: calc(100% / 3 - 50px);
				line-height: 40px;
				position: relative;
				height: auto;
				.icon {
					padding: 0 5px;
					color: #FFFFFF;
					display: none;
					font-size: 14px;
				}
				.label {
					color: #FFFFFF;
					display: inline-block;
					font-size: 14px;
				}
				.text {
					padding: 0 0 0 5px;
					color: #FFFFFF;
					display: inline-block;
					font-size: 14px;
					text-align: right;
				}
			}
			.info-item3 {
				padding: 0 20px;
				z-index: 1;
				display: inline-block;
				width: calc(100% / 3 - 50px);
				line-height: 40px;
				position: relative;
				height: auto;
				.icon {
					padding: 0 5px;
					color: #FFFFFF;
					display: none;
					font-size: 14px;
				}
				.label {
					color: #FFFFFF;
					display: inline-block;
					font-size: 14px;
				}
				.text {
					padding: 0 0 0 5px;
					color: #FFFFFF;
					display: inline-block;
					font-size: 14px;
					text-align: right;
				}
			}
			.info-item4 {
				padding: 0 20px;
				z-index: 1;
				display: inline-block;
				width: calc(100% / 3 - 50px);
				line-height: 40px;
				position: relative;
				height: auto;
				.icon {
					padding: 0 5px;
					color: #FFFFFF;
					display: none;
					font-size: 14px;
				}
				.label {
					color: #FFFFFF;
					display: inline-block;
					font-size: 14px;
				}
				.text {
					padding: 0 0 0 5px;
					color: #FFFFFF;
					display: inline-block;
					font-size: 14px;
					text-align: right;
				}
			}
			.info-item5 {
				padding: 0 20px;
				z-index: 1;
				display: inline-block;
				width: calc(100% / 3 - 50px);
				line-height: 40px;
				position: relative;
				height: auto;
				.icon {
					padding: 0 5px;
					color: #FFFFFF;
					display: none;
					font-size: 14px;
				}
				.label {
					color: #FFFFFF;
					display: inline-block;
					font-size: 14px;
				}
				.text {
					padding: 0 0 0 5px;
					color: #FFFFFF;
					display: inline-block;
					font-size: 14px;
					text-align: right;
				}
			}
			.info-item6 {
				padding: 0 20px;
				z-index: 1;
				display: inline-block;
				width: calc(100% / 3 - 10px);
				line-height: 40px;
				position: relative;
				height: auto;
				.icon {
					padding: 0 5px;
					color: #FFFFFF;
					display: none;
					font-size: 14px;
				}
				.label {
					color: #FFFFFF;
					display: inline-block;
					font-size: 14px;
				}
				.text {
					padding: 0 0 0 5px;
					color: #FFFFFF;
					display: inline-block;
					font-size: 14px;
					text-align: right;
				}
			}
		}
		.center-tabs.el-tabs {
			border: 1px solid #BBB09B;
			border-radius: 0;
			padding: 0 0 20px 0;
			margin: 20px 0 0 0;
			background: #CCDAF1;
			display: flex;
			flex-wrap: wrap;
			/deep/ .el-tabs__header {
				border-radius: 0px 0px 20px 20px;
				padding: 10px 20px;
				margin: 0;
				background: #FFD99D;
				width: 100%;
				position: relative;
				float: left;
			}
			/deep/ .el-tabs__header .el-tabs__item {
				padding: 0 30px 0 20px;
				margin: 0 10px;
				color: #000;
				background: none;
				font-weight: 500;
				display: inline-block;
				font-size: 16px;
				line-height: 40px;
				position: relative;
				text-align: center;
				height: 40px;
			}
			/deep/ .el-tabs__header .el-tabs__item:hover {
				padding: 0 30px 0 20px;
				margin: 0 10px;
				background-size: 100% 100%;
				color: #fff;
				background: url(http://codegen.caihongy.cn/20241207/fb81969a60fe4753916f2a29316c041e.png) center center/cover;
				font-weight: 500;
				display: inline-block;
				font-size: 16px;
				line-height: 40px;
				position: relative;
				text-align: center;
				height: 40px;
			}
			/deep/ .el-tabs__header .el-tabs__item.is-active {
				padding: 0 30px 0 20px;
				margin: 0 10px;
				background-size: 100% 100%;
				color: #fff;
				background: url(http://codegen.caihongy.cn/20241207/fb81969a60fe4753916f2a29316c041e.png) center center/cover;
				font-weight: 500;
				display: inline-block;
				font-size: 16px;
				line-height: 40px;
				position: relative;
				text-align: center;
				height: 40px;
			}
			/deep/ .el-tabs__content {
				padding: 20px 0;
				background: none;
				width: 100%;
			}
			/deep/ .el-tabs__content .el-tab-pane {
				padding: 20px 100px 20px 20px;
				width: 100%;
			}
			& /deep/ .el-tabs__header {
				.el-tabs__nav{
					overflow: auto;
				}
				::-webkit-scrollbar {
					-webkit-appearance: none;
					width: 6px;
					height: 6px;
				}
				::-webkit-scrollbar-track {
					background: rgba(0, 0, 0, 0.1);
					border-radius: 0;
				}
				::-webkit-scrollbar-thumb {
					cursor: pointer;
					border-radius: 5px;
					background: rgba(0, 0, 0, 0.15);
					transition: color 0.2s ease;
				}
				::-webkit-scrollbar-thumb:hover {
					background: rgba(0, 0, 0, 0.3);
				}
				.el-tabs__nav-wrap {
					margin: 0;
					&::after {
						content: none;
					}
				}
				.el-tabs__active-bar {
					display: none !important;
				}
			}
			.center-preview-pv {
				.center-item.el-form-item {
					padding: 10px;
					margin: 0 0 10px;
					background: none;
					display: inline-block;
					width: 100%;
					/deep/ .el-form-item__label {
						padding: 0 10px 0 0;
						margin: 0;
						color: #000;
						font-weight: 500;
						width: 180px;
						font-size: 16px;
						line-height: 50px;
						text-align: right;
					}
					.el-form-item__content {
						margin-left: 180px;
					}
					.el-input {
						width: 100%;
					}
					.el-input /deep/ .el-input__inner {
						border: 0px solid #BBB09B;
						border-radius: 10px;
						padding: 0 12px;
						box-shadow: 0 0 0px rgba(64, 158, 255, .5);
						outline: none;
						color: #000;
						width: 100%;
						font-size: 15px;
						line-height: 50px;
						height: 50px;
					}
					.el-input /deep/ .el-input__inner[readonly="readonly"] {
						border: 0px solid #BBB09B;
						cursor: not-allowed;
						border-radius: 10px;
						padding: 0 12px;
						box-shadow: 0 0 0px rgba(85, 85, 127, 0.5);
						outline: none;
						color: #000;
						background: #FFFFFF;
						width: 100%;
						font-size: 15px;
						height: 50px;
					}
					.el-select {
						width: 100%;
					}
					.el-select /deep/ .el-input__inner {
						border: 0px solid #BBB09B;
						border-radius: 10px;
						padding: 0 10px;
						box-shadow: 0 0 0px rgba(64, 158, 255, .5);
						outline: none;
						color: #000;
						background: #FFFFFF;
						width: 100%;
						font-size: 15px;
						height: 50px;
					}
					.el-select /deep/ .is-disabled .el-input__inner {
						border: 0px solid #BBB09B;
						cursor: not-allowed;
						border-radius: 10px;
						padding: 0 10px;
						box-shadow: 0 0 0px rgba(85, 85, 127, 0.5);
						outline: none;
						color: #000;
						background: #FFFFFF;
						width: 100%;
						font-size: 15px;
						height: 50px;
					}
					.el-date-editor {
						width: 100%;
					}
					.el-date-editor /deep/ .el-input__inner {
						border: 0px solid #BBB09B;
						border-radius: 10px;
						padding: 0 10px 0 30px;
						box-shadow: 0 0 0px rgba(64, 158, 255, .5);
						outline: none;
						color: #000;
						background: #FFFFFF;
						width: 100%;
						font-size: 15px;
						height: 50px;
					}
					.el-date-editor /deep/ .el-input__inner[readonly="readonly"] {
						border: 0px solid #BBB09B;
						cursor: not-allowed;
						border-radius: 10px;
						padding: 0 10px 0 30px;
						box-shadow: 0 0 0px rgba(85, 85, 127, 0.5);
						outline: none;
						color: #000;
						background: #FFFFFF;
						width: 100%;
						font-size: 15px;
						height: 50px;
					}
					/deep/ .el-upload--picture-card {
						background: transparent;
						border: 0;
						border-radius: 0;
						width: auto;
						height: auto;
						line-height: initial;
						vertical-align: middle;
					}
					/deep/ .upload .upload-img {
						border: 0px solid #BBB09B;
						cursor: pointer;
						border-radius: 6px;
						color: #000;
						background: #FFFFFF;
						object-fit: cover;
						width: 90px;
						font-size: 32px;
						line-height: 80px;
						text-align: center;
						height: 80px;
					}
					/deep/ .el-upload-list .el-upload-list__item {
						border: 0px solid #BBB09B;
						cursor: pointer;
						border-radius: 6px;
						color: #000;
						background: #FFFFFF;
						object-fit: cover;
						width: 90px;
						font-size: 32px;
						line-height: 80px;
						text-align: center;
						height: 80px;
						font-size: 14px;
						line-height: 1.8;
					}
					/deep/ .el-upload .el-icon-plus {
						border: 0px solid #BBB09B;
						cursor: pointer;
						border-radius: 6px;
						color: #000;
						background: #FFFFFF;
						object-fit: cover;
						width: 90px;
						font-size: 32px;
						line-height: 80px;
						text-align: center;
						height: 80px;
					}
					/deep/ .el-upload__tip {
						color: #333;
						line-height: 1;
					}
					/deep/ .el-input__inner::placeholder {
						color: #999;
						font-size: 15px;
					}
					.balance-item {
						display: flex;
						.el-input {
							width: calc(100% - 110px);
						}
						.el-input /deep/ .el-input__inner {
							border: 0px solid #BBB09B;
							border-radius: 10px;
							padding: 0 12px;
							box-shadow: 0 0 0px rgba(64, 158, 255, .5);
							outline: none;
							color: #000;
							display: inline-block;
							width: 100%;
							font-size: 15px;
							height: 50px;
						}
						.balanceBtn {
							border: 0;
							cursor: pointer;
							padding: 0;
							margin: 0 0 0 10px;
							color: #44446D;
							display: inline-block;
							font-size: 14px;
							line-height: 50px;
							border-radius: 10px;
							outline: none;
							background: #FFFFFF;
							width: 100px;
							text-align: center;
							height: 50px;
							.icon {
								color: rgba(255, 255, 255, 1);
								display: none;
							}
							.text {
								color: #44446D;
							}
						}
						.balanceBtn:hover {
							opacity: 0.5;
							.icon {
								color: #000;
							}
							.text {
								color: #fff;
							}
						}
					}
				}
				.center-btn-item {
					padding: 0;
					margin: 0;
					display: flex;
					justify-content: center;
					text-align: center;
					.updateBtn {
						border: 0;
						cursor: pointer;
						padding: 0 35px;
						margin: 0 20px 0 0;
						display: inline-block;
						font-size: 14px;
						line-height: 50px;
						border-radius: 20px;
						outline: none;
						background: #44446D;
						width: 150px;
						height: 50px;
						order: 1;
						.icon {
							color: rgba(255, 255, 255, 1);
							display: none;
						}
						.text {
							color: rgba(255, 255, 255, 1);
						}
					}
					.updateBtn:hover {
						opacity: 0.5;
						.icon {
							color: #000;
						}
						.text {
							color: #fff;
						}
					}
					.closeBtn {
						border: 0;
						cursor: pointer;
						border-radius: 20px;
						padding: 0 35px;
						margin: 0 20px 0 0;
						outline: none;
						background: #9D8F79;
						display: inline-block;
						width: 150px;
						font-size: 14px;
						line-height: 50px;
						height: 50px;
						.icon {
							color: rgba(64, 158, 255, 1);
							display: none;
						}
						.text {
							color: #fff;
						}
					}
					.closeBtn:hover {
						opacity: 0.5;
						.icon {
							color: rgba(64, 158, 255, 0.5);
						}
						.text {
							color: #fff;
						}
					}
				}
				.el-date-editor.el-input {
					width: auto;
				}
			}
		}
	}
</style>
