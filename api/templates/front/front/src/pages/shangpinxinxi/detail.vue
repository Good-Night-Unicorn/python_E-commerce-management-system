<template>
	<div>
	<!--  -->
		<div class="breadcrumb-preview">
			<el-breadcrumb :separator="''">
				<el-breadcrumb-item class="item1" to="/"><a>首页</a></el-breadcrumb-item>
				<el-breadcrumb-item class="item2" v-for="(item, index) in breadcrumbItem" :key="index" :to="'/index/shangpinxinxi?centerType=' + (centerType?'1':'0')"><a>{{item.name}}</a></el-breadcrumb-item>
				<el-breadcrumb-item class="item3"><a href="javascript:void(0);">详情</a></el-breadcrumb-item>
			</el-breadcrumb>
		</div>
		<div class="back_box">
			<el-button class="backBtn" size="mini" @click="backClick">
				<span class="icon iconfont icon-jiantou33"></span>
				<span class="text">返回</span>
			</el-button>
		</div>
		<div class="detail-preview">
			<div class="attr">
				<div class="info">
					<div class="title-item">
						<div class="detail-title">
							{{detail.shangpinmingcheng}}
						</div>
						<div class="colectBtn" @click="storeup(1)" v-show="!isStoreup">
							<i class="icon iconfont icon-shoucang10"></i>
							<span class="text">收藏({{detail.storeupnum}})</span>
						</div>
						<div class="colectBtnActive" @click="storeup(-1)" v-show="isStoreup">
							<i class="icon iconfont icon-shoucang12"></i>
							<span class="text">已收藏({{detail.storeupnum}})</span>
						</div>
					</div>
					<div class="item" v-if="detail.price">
						<div class="lable">价格</div>
						<div class="text price bold"><span style="font-size: 12px">￥</span>{{detail.price}}</div>
					</div>
					<div class="item" v-if="detail.jf">
						<div class="lable">积分</div>
						<div class="text price bold">{{detail.jf}}</div>
					</div>
					<div class="item">
						<div class="lable">单限</div>
						<div class="text">{{detail.onelimittimes}}</div>
					</div>
					<div class="item">
						<div class="lable">库存</div>
						<div class="text">{{detail.alllimittimes}}</div>
					</div>
					<div class="item">
						<div class="lable">商品编号</div>
						<div class="text "  >{{detail.shangpinbianhao}}</div>
					</div>
					<div class="item">
						<div class="lable">商品类型</div>
						<div class="text "  >{{detail.shangpinleixing}}</div>
					</div>
					<div class="item">
						<div class="lable">规格</div>
						<div class="text "  >{{detail.guige}}</div>
					</div>
					<div class="item">
						<div class="lable">发布时间</div>
						<div class="text "  >{{detail.fabushijian}}</div>
					</div>
					<div class="item">
						<div class="lable">点击次数</div>
						<div class="text "  >{{detail.clicknum}}</div>
					</div>
					<div class="btn_box">
						<el-input-number v-if="detail.alllimittimes" :min=1 v-model="buynumber"></el-input-number>
						<el-button class="addCartBtn" v-if="detail.alllimittimes" type="warning" size="small" @click="addCart">添加到购物车</el-button>
						<el-button class="buyBtn" v-if="detail.alllimittimes" type="warning" size="small" @click="buyNow">立即购买</el-button>

					</div>
					<div class="btn_box">
						<el-button class="editBtn" v-if="btnAuth('shangpinxinxi','修改')" @click="editClick">修改</el-button>
						<el-button class="delBtn" v-if="btnAuth('shangpinxinxi','删除')" @click="delClick">删除</el-button>
					</div>
				</div>
			</div>
		
			<el-carousel v-if="detailBanner.length" trigger="click" indicator-position="inside" arrow="always" type="default" direction="horizontal" height="600px" :autoplay="false" :interval="3000" :loop="true">
				<el-carousel-item v-for="item in detailBanner" :key="item.id">
					<img :preview-src-list="[item]" v-if="item.substr(0,4)=='http'" :src="item" class="image">
					<img :preview-src-list="[baseUrl + item]" v-else :src="baseUrl + item" class="image">
				</el-carousel-item>
			</el-carousel>

			<div class="zancai">
				<div v-if="!isThumbsupnum && !isCrazilynum" class="zan" @click="thumbsupOrCrazily(21)">
					<i class="icon iconfont icon-zan07"></i>
					<span class="text">赞一下({{detail.thumbsupnum}})</span>
				</div>
				<div v-if="!isThumbsupnum && !isCrazilynum" class="cai" @click="thumbsupOrCrazily(22)">
					<i class="icon iconfont icon-cai01"></i>
					<span class="text">踩一下({{detail.crazilynum}})</span>
				</div>
				<div v-if="isThumbsupnum" class="zanActive" @click="cancelThumbsupOrCrazily(21)">
					<i class="icon iconfont icon-zan11"></i>
					<span class="text">已赞({{detail.thumbsupnum}})</span>
				</div>
				<div v-if="isCrazilynum" class="caiActive" @click="cancelThumbsupOrCrazily(22)">
					<i  class="icon iconfont icon-cai16"></i>
					<span class="text">已踩({{detail.crazilynum}})</span>
				</div>
			</div>

		

			<el-tabs class="detail-tabs" v-model="activeName" type="border-card" v-if="tabsNum>0" >
				<el-tab-pane label="商品介绍" name="first">
					<div class="ql-snow ql-editor" v-html="detail.shangpinjieshao"></div>
				</el-tab-pane>
				<el-tab-pane label="评论" name="second">
					<el-form class="add commentForm" :model="form" :rules="rules" ref="form">
						<el-form-item class="item" label="评论" prop="content">
							<editor
								myQuillEditor="content"
								v-model="form.content" 
								class="editor" 
								action="file/upload">
							</editor>
						</el-form-item>
						<el-form-item class="commentBtn">
							<el-button class="submitBtn" type="primary" @click="submitForm('form')">立即提交</el-button>
							<el-button class="resetBtn" @click="resetForm('form')">重置</el-button>
						</el-form-item>
					</el-form>
				
					<div v-if="infoList.length" class="comment-list">
						<div class="comment-item" v-for="item in infoList" :key="item.id" @mouseenter="discussEnter(item.id)"
							@mouseleave="discussLeave">
							<div class="istop" v-if="item.istop">
								<span class="icon iconfont icon-jiantou24"></span>
							</div>
							<div class="user">
								<el-image v-if="item.avatarurl" :size="50" :src="baseUrl + item.avatarurl"></el-image>
								<el-image v-if="!item.avatarurl" :size="50" :src="require('@/assets/touxiang.png')"></el-image>
								<div class="name">{{item.nickname}}</div>
							</div>
							<div class="comment-content-box">
								<div class="ql-snow ql-editor" v-html="item.content"></div>
								<div class="comment-time">{{item.addtime}}</div>
								<div class="zancai-box">
									<div v-if="!comcaiChange(item)" class="zan-item" :class="comzanChange(item)?'active':''" @click="comzanClick(item)">
										<span class="icon iconfont" :class="comzanChange(item)?'icon-zan11':'icon-zan07'"></span>
										<span class="label">{{comzanChange(item)?'已赞':'赞'}}</span>
										<span class="num">({{item.thumbsupnum}})</span>
									</div>
									<div v-if="!comzanChange(item)" class="cai-item" :class="comcaiChange(item)?'active':''" @click="comcaiClick(item)">
										<span class="icon iconfont" :class="comcaiChange(item)?'icon-cai16':'icon-cai01'"></span>
										<span class="label">{{comcaiChange(item)?'已踩':'踩'}}</span>
										<span class="num">({{item.crazilynum}})</span>
									</div>
								</div>
								<div class="comment-btn">
									<!-- <el-button :style='{"border":"0","cursor":"pointer","padding":"0 20px","margin":"0","outline":"none","color":"rgba(255, 255, 255, 1)","borderRadius":"0","background":"#BBB09B","width":"auto","lineHeight":"30px","fontSize":"14px","height":"30px"}'>回复</el-button> -->
									<el-button class="delBtn" v-if="showIndex==item.id&&userid==item.userid" @click="discussDel(item.id)">删除</el-button>
								</div>
							</div>
							<div class="comment-content-box" v-if="item.reply">
								回复：<span class="ql-snow ql-editor" v-html="item.reply"></span>
							</div>
						</div>
					</div>
				
					<el-pagination
						background
						id="pagination" class="pagination"
						:page-size="pageSize"
						prev-text="上一页"
						next-text="下一页"
						:hide-on-single-page="true"
						:layout='["total","prev","pager","next"].join()'
						:total="total"
						@current-change="curChange"
						@prev-click="prevClick"
						@next-click="nextClick"
						@size-change="sizeChange"
						></el-pagination>
				</el-tab-pane>
			</el-tabs>

		</div>
		<div class="share_view">
		</div>
	</div>
</template>

<script>
	import axios from 'axios'
	import Swiper from "swiper";
	export default {
		//数据集合
		data() {
			return {
				tablename: 'shangpinxinxi',
				baseUrl: '',
				breadcrumbItem: [
					{
						name: '商品信息'
					}
				],
				title: '',
				detailBanner: [],
				userid: Number(localStorage.getItem('frontUserid')),
				id: 0,
				detail: {},
				tabsNum: 2,
				activeName: 'second',
				form: {
					content: '',
					userid: Number(localStorage.getItem('frontUserid')),
					nickname: localStorage.getItem('username'),
					avatarurl: '',
				},
				showIndex: -1,
				infoList: [],
				rules: {
					content: [
						{ required: true, message: '请输入内容', trigger: 'blur' }
					],
				},
				total: 1,
				pageSize: 10,
				totalPage: 1,
				storeupParams: {
					name: '',
					picture: '',
					refid: 0,
					tablename: 'shangpinxinxi',
					userid: Number(localStorage.getItem('frontUserid'))
				},
				isStoreup: false,
				storeupInfo: {},
				isCrazilynum: false,
				isThumbsupnum: false,
				thumbsupOrCrazilyInfo: {},
				buynumber: 1,
				cart: {
					buynumber: 0,
					discountprice: 0,
					goodid: 0,
					goodname: '',
					picture: '',
					price: 0,
					userid: Number(localStorage.getItem('frontUserid'))
				},
				isInCart: false,
				centerType: false,
				storeupType: false,
				shareUrl: location.href,
			}
		},
		created() {
			if(this.$route.query.centerType&&this.$route.query.centerType!=0) {
				this.centerType = true
			}
			if(this.$route.query.storeupType&&this.$route.query.storeupType!=0) {
				this.storeupType = true
			}
			
			this.init();
		},
		mounted() {
		},
		//方法集合
		methods: {
			init() {
				this.id = this.$route.query.id
				this.baseUrl = this.$config.baseUrl;
				this.$http.get(this.tablename + '/detail/'  + this.id, {}).then(res => {
					if (res.data.code == 0) {
						this.detail = res.data.data;
						this.title = this.detail.shangpinmingcheng;
						if(this.detail.tupian) {
							this.detailBanner = this.detail.tupian.split(",w").length>1?[this.detail.tupian]:this.detail.tupian.split(',');
						}
						this.$forceUpdate();
						this.getDiscussList(1);
						if(localStorage.getItem('frontToken')){
							this.getStoreupStatus();
							this.getThumbsupOrCrazilyStatus();
							this.getCartList();
						}

					}
				});
			},
			storeup(type) {
				if (type == 1 && !this.isStoreup) {
					this.storeupParams.name = this.title;
					this.storeupParams.picture = this.detailBanner[0];
					this.storeupParams.refid = this.detail.id;
					this.storeupParams.type = String(type);
					this.$http.post('storeup/add', this.storeupParams).then(res => {
						if (res.data.code == 0) {
							this.isStoreup = true;
							this.detail.storeupnum++
							this.$http.post('shangpinxinxi/update', this.detail).then(res => {});
							this.$message({
								type: 'success',
								message: '收藏成功!',
								duration: 1500,
							});
						}
					});
				}
				if (type == -1 && this.isStoreup) {
					this.$http.get('storeup/list', {params: {page: 1, limit: 1, type: '1', refid: this.detail.id, tablename: 'shangpinxinxi', userid: Number(localStorage.getItem('frontUserid'))}}).then(res => {
						if (res.data.code == 0 && res.data.data.list.length > 0) {
							this.isStoreup = true;
							this.storeupInfo = res.data.data.list[0];
							let delIds = new Array();
							delIds.push(this.storeupInfo.id);
							this.$http.post('storeup/delete', delIds).then(res => {
								if (res.data.code == 0) {
									this.isStoreup = false;
									this.detail.storeupnum--
									this.$http.post('shangpinxinxi/update', this.detail).then(res => {});
									this.$message({
										type: 'success',
										message: '取消成功!',
										duration: 1500,
									});
								}
							});
						}
					});
				}
			},
			getStoreupStatus(){
				if(localStorage.getItem("frontToken")) {
					this.$http.get('storeup/list', {params: {page: 1, limit: 1, type: '1', refid: this.detail.id, tablename: 'shangpinxinxi', userid: Number(localStorage.getItem('frontUserid'))}}).then(res => {
						if (res.data.code == 0 && res.data.data.list.length > 0) {
							this.isStoreup = true;
							this.storeupInfo = res.data.data.list[0];
						}
					});
				}
			},
			thumbsupOrCrazily(type) {
				this.storeupParams.name = this.title;
				this.storeupParams.picture = this.detailBanner[0];
				this.storeupParams.refid = this.detail.id;
				this.storeupParams.type = String(type);
				this.$http.post('storeup/add', this.storeupParams).then(res => {
					if (res.data.code == 0) {
						this.getThumbsupOrCrazilyStatus();
						this.$message({
							type: 'success',
							message: '操作成功!',
							duration: 1500,
						});
					}
				});

				if (type == 21) this.detail.thumbsupnum = Number(this.detail.thumbsupnum) + 1;
				if (type == 22) this.detail.crazilynum = Number(this.detail.crazilynum) + 1;
				this.$http.post('shangpinxinxi/update', this.detail).then(res => {});
			},
			cancelThumbsupOrCrazily(type) {
				let delIds = new Array();
				delIds.push(this.thumbsupOrCrazilyInfo.id);
				this.$http.post('storeup/delete', delIds).then(res => {
					if (res.data.code == 0) {
						this.isThumbsupnum = false;
						this.isCrazilynum = false;
						this.$message({
							type: 'success',
							message: '取消成功!',
							duration: 1500,
						});
					}
				});
				if (type == 21) this.detail.thumbsupnum -= 1;
				if (type == 22) this.detail.crazilynum -= 1;
				this.$http.post('shangpinxinxi/update', this.detail).then(res => {});
			},
			getThumbsupOrCrazilyStatus() {
				if(localStorage.getItem("frontToken")) {
					this.$http.get('storeup/list', {params: {page: 1, limit: 1, type: '21', refid: this.detail.id, tablename: 'shangpinxinxi', userid: Number(localStorage.getItem('frontUserid'))}}).then(res => {
						if (res.data.code == 0 && res.data.data.list.length > 0) {
							this.isThumbsupnum = true;
							this.thumbsupOrCrazilyInfo = res.data.data.list[0];
						}
					});
					this.$http.get('storeup/list', {params: {page: 1, limit: 1, type: '22', refid: this.detail.id, tablename: 'shangpinxinxi', userid: Number(localStorage.getItem('frontUserid'))}}).then(res => {
						if (res.data.code == 0 && res.data.data.list.length > 0) {
							this.isCrazilynum = true;
							this.thumbsupOrCrazilyInfo = res.data.data.list[0];
						}
					});
				}
			},
			curChange(page) {
				this.getDiscussList(page);
			},
			prevClick(page) {
				this.getDiscussList(page);
			},
			nextClick(page) {
				this.getDiscussList(page);
			},
			sizeChange(size){
				this.pageSize = size
				this.getDiscussList(1);
			},
			// 返回按钮
			backClick(){
				if(this.storeupType){
					history.back()
				}else{
					let params = {}
					if(this.centerType){
						params.centerType = 1
					}
					this.$router.push({path: '/index/shangpinxinxi', query: params});
				}
			},
			// 下载
			download(file ){
				if(!file) {
					this.$message({
						type: 'error',
						message: '文件不存在',
						duration: 1500,
					});
					return;
				}
				let arr = file.replace(new RegExp('upload/', "g"), "")
				axios.get(this.baseUrl + '/file/download?fileName=' + arr, {
					headers: {
						token: localStorage.getItem("frontToken")
					},
					responseType: "blob"
				}).then(({
					data
				}) => {
					const binaryData = [];
					binaryData.push(data);
					const objectUrl = window.URL.createObjectURL(new Blob(binaryData, {
						type: 'application/pdf;chartset=UTF-8'
					}))
					const a = document.createElement('a')
					a.href = objectUrl
					a.download = arr
					// a.click()
					// 下面这个写法兼容火狐
					a.dispatchEvent(new MouseEvent('click', {
						bubbles: true,
						cancelable: true,
						view: window
					}))
					window.URL.revokeObjectURL(data)
				},err=>{
					axios.get((location.href.split(this.$config.name).length>1 ? location.href.split(this.$config.name)[0] :'') + this.$config.name + '/file/download?fileName=' + arr, {
						headers: {
							token: localStorage.getItem("frontToken")
						},
						responseType: "blob"
					}).then(({
						data
					}) => {
						const binaryData = [];
						binaryData.push(data);
						const objectUrl = window.URL.createObjectURL(new Blob(binaryData, {
							type: 'application/pdf;chartset=UTF-8'
						}))
						const a = document.createElement('a')
						a.href = objectUrl
						a.download = arr
						// a.click()
						// 下面这个写法兼容火狐
						a.dispatchEvent(new MouseEvent('click', {
							bubbles: true,
							cancelable: true,
							view: window
						}))
						window.URL.revokeObjectURL(data)
					})
				})
			},
			getDiscussList(page) {
				this.$http.get('discussshangpinxinxi/list', {params: {page, limit: this.pageSize, refid: this.detail.id,sort: 'istop',order: 'desc'}}).then(res => {
					if (res.data.code == 0) {
						this.infoList = res.data.data.list;
						this.total = res.data.data.total;
						this.pageSize = Number(res.data.data.pageSize);
						this.totalPage = res.data.data.totalPage;
					}
				});
			},
			comzanChange(row){
				if(row.tuserids){
					let arr = row.tuserids.split(',')
					for(let x in arr){
						if(arr[x] == this.userid){
							return true
						}
					}
				}
				return false
			},
			comzanClick(row){
				if(!this.userid){
					return false
				}
				if(!this.comzanChange(row)){
					row.thumbsupnum++
					if(row.tuserids){
						row.tuserids = row.tuserids + ',' + this.userid
					}else {
						row.tuserids = String(this.userid)
					}
					this.$http.post('discussshangpinxinxi/update',row).then(rs=>{
						this.$message.success('点赞成功')
					})
				}else {
					row.thumbsupnum--
					let arr = row.tuserids.split(',')
					for(let x in arr){
						if(arr[x] == this.userid){
							arr.splice(x,1)
						}
					}
					row.tuserids = arr.join(',')
					this.$http.post('discussshangpinxinxi/update',row).then(rs=>{
						this.$message.success('取消成功')
					})
				}
			},
			comcaiChange(row){
				if(row.cuserids){
					let arr = row.cuserids.split(',')
					for(let x in arr){
						if(arr[x] == this.userid){
							return true
						}
					}
				}
				return false
			},
			comcaiClick(row){
				if(!this.userid){
					return false
				}
				if(!this.comcaiChange(row)){
					row.crazilynum++
					if(row.cuserids){
						row.cuserids = row.cuserids + ',' + this.userid
					}else {
						row.cuserids = String(this.userid)
					}
					this.$http.post('discussshangpinxinxi/update',row).then(rs=>{
						this.$message.success('点踩成功')
					})
				}else {
					row.crazilynum--
					let arr = row.cuserids.split(',')
					for(let x in arr){
						if(arr[x] == this.userid){
							arr.splice(x,1)
						}
					}
					row.cuserids = arr.join(',')
					this.$http.post('discussshangpinxinxi/update',row).then(rs=>{
						this.$message.success('取消成功')
					})
				}
			},
			discussEnter(index){
				this.showIndex = index
			},
			discussLeave(){
				this.showIndex = -1
			},
			discussDel(id){
				this.$confirm('是否删除此评论？').then(_ => {
					this.$http.post('discussshangpinxinxi/delete',[id]).then(res=>{
						if(res.data&&res.data.code==0){
							this.addDiscussNum(1)
							this.$message({
								type: 'success',
								message: '删除成功!',
								duration: 1500,
								onClose: () => {
									this.getDiscussList(1);
								}
							});
						}
					})
				}).catch(_ => {});
			},
			submitForm(formName) {
				this.$refs[formName].validate((valid) => {
					if (valid) {
						this.$http.get('orders/list', {params: {page: 1, limit: 1, status: '已完成', goodid: this.detail.id, userid: Number(localStorage.getItem('frontUserid'))}}).then(res => {
							if (res.data.code == 0 && res.data.data.list.length == 0) {
								this.$message({
									type: 'error',
									message: '请完成订单后再评论!',
									duration: 1500
								});
								return false
							} else {
								this.form.refid = this.detail.id;
								this.form.avatarurl = localStorage.getItem('frontHeadportrait')?localStorage.getItem('frontHeadportrait'):'';
								this.$http.post('discussshangpinxinxi/add', this.form).then(rs2 => {
									if (rs2.data.code == 0) {
										this.addDiscussNum(2)
										this.form.content = '';
										this.getDiscussList(1);
										this.$message({
											type: 'success',
											message: '评论成功!',
											duration: 1500,
										});
									}
								});
							}
						});
					} else {
						return false;
					}
				});
			},
			resetForm(formName) {
				this.$refs[formName].resetFields();
			},
			addDiscussNum(type){
				if(type==2){
					this.detail.discussnum++
				}else if(type==1){
					if(this.detail.discussnum!=0){
						this.detail.discussnum--
					}else{
						this.detail.discussnum = 0
					}
				}
				this.$http.post('shangpinxinxi/update',this.detail).then(res=>{})
			},
			getCartList() {
				this.$http.get('cart/list', {params: {userid: Number(localStorage.getItem('frontUserid')), tablename: 'shangpinxinxi', goodid: this.detail.id}}).then(res => {
					if (res.data.code == 0) {
						if (res.data.data.list.length > 0) {
							this.isInCart = true;
						} else {
							this.isInCart = false;
						}
					}
				});
			},
			addCart() {
				// 单次购买限制
				if (this.detail.onelimittimes > 0 && this.detail.onelimittimes < this.buynumber) {
					this.$message.error(`每人单次只能购买${this.detail.onelimittimes}件`);
					return
				}
				// 库存不够
				if (this.detail.alllimittimes <= 0 ) {
					this.$message.error(`商品已售罄`);
					return
				}
				// 库存限制
				if (this.detail.alllimittimes > 0 && this.detail.alllimittimes < this.buynumber) {
					this.$message.error(`库存不足`);
					return
				}
				if (this.isInCart) {
					this.$message.error('该商品已经添加到购物车');
					return;
				}
		
				this.cart.buynumber = this.buynumber;
				this.cart.goodid = this.detail.id;
				this.cart.goodname = this.title;
				this.cart.tablename = this.tablename;
				this.cart.picture = this.detailBanner[0];
				this.cart.price = this.detail.price;
				this.cart.discountprice = this.detail.vipprice?this.detail.vipprice:this.detail.price;
				this.$http.post('cart/save', this.cart).then(res => {
					if (res.data.code === 0) {
						this.getCartList();
						this.$message({
							message: '添加成功',
							type: 'success',
							duration: 1500,
						});
					} else {
						this.$message.error(res.data.msg);
					}
				});
			},
			//立即购买
			buyNow() {
				// 单次购买限制
				if (this.detail.onelimittimes > 0 && this.detail.onelimittimes < this.buynumber) {
					this.$message.error(`每人单次只能购买${this.detail.onelimittimes}件`);
					return
				}
				// 库存不够
				if (this.detail.alllimittimes <= 0 ) {
					this.$message.error(`商品已售罄`);
					return
				}
				// 库存限制
				if (this.detail.alllimittimes > 0 && this.detail.alllimittimes < this.buynumber) {
					this.$message.error(`库存不足`);
					return
				}
				// 保存到storage中，在确认下单页面中获取要购买的商品
				localStorage.setItem('orderGoods', JSON.stringify([{
					tablename: this.tablename,
					goodid: this.detail.id,
					goodname: this.title,

					picture:this.detailBanner[0],
					buynumber: this.buynumber,
					userid: Number(localStorage.getItem('frontUserid')),
					price: this.detail.price,
					discountprice: this.detail.vipprice ? this.detail.vipprice : this.detail.price
				}]));
				// 跳转到确认下单页面
				let query = {
					type: 1,
				}
				this.$router.push({path: '/index/shop-order/orderConfirm', query: query});
			},


			// 权限判断
			btnAuth(tableName,key){
				if(this.centerType){
					return this.isBackAuth(tableName,key)
				}else{
					return this.isAuth(tableName,key)
				}
			},
			// 修改
			editClick(){
				this.$router.push(`/index/shangpinxinxiAdd?type=edit&&id=${this.detail.id}`);
			},
			// 删除
			async delClick(){
				await this.$confirm('是否删除此商品信息？') .then(_ => {
					this.$http.post('shangpinxinxi/delete', [this.detail.id]).then(async res => {
						if (res.data.code == 0) {
							this.$http.get('storeup/list',{params:{
								page: 1,
								limit: 100,
								refid: this.detail.id,
								tablename: 'shangpinxinxi',
							}}).then(async obj=>{
								if(obj.data&&obj.data.code==0){
									let arr = []
									for(let x in obj.data.data.list){
										arr.push(obj.data.data.list[x].id)
									}
									if(arr.length){
										await this.$http.post('storeup/delete',arr).then(()=>{})
									}
									this.$message({
										type: 'success',
										message: '删除成功!',
										duration: 1500,
										onClose: () => {
											history.back()
										}
									});
								}
							})
						}
					});
				}).catch(_ => {});
			},
		},
		components: {
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.detail-preview {
		padding: 30px calc((100% - 1200px)/2);
		margin: 0px auto;
		background: #EDF0FA;
		display: flex;
		width: 100%;
		position: relative;
		flex-wrap: wrap;
		.attr {
			border: 1px solid #2D2D65;
			padding: 0;
			margin: 0 0 0 10px;
			background: #CCDAF1;
			display: flex;
			width: calc(50% - 10px);
			position: relative;
			order: 3;
			.info {
				margin: 0;
				background: #CCDAF1;
				flex: 1;
				display: flex;
				justify-content: space-between;
				flex-wrap: wrap;
				.title-item {
					padding: 0px 20px;
					margin: 0 0 10px 0;
					display: flex;
					width: 100%;
					border-color: #44446D;
					border-width: 0 0 1px 0;
					justify-content: space-between;
					align-items: center;
					border-style: solid;
					.detail-title {
						color: #000;
						font-weight: 400;
						font-size: 16px;
					}
					.colectBtn {
						cursor: pointer;
						border-radius: 50%;
						padding: 0;
						background: #44446D;
						width: 40px;
						text-align: center;
						height: 40px;
						.icon {
							color: #fff;
							font-size: 14px;
							line-height: 40px;
						}
						.text {
							color: #999;
							display: none;
							font-size: 14px;
						}
					}
					.colectBtnActive {
						background: #F9B20E;
						.icon {
							color: #fff;
						}
						.text {
							color: #fff;
						}
					}
					.colectBtn:hover {
						background: #F9B20E90;
						.icon {
							color: #fff;
						}
						.text {
							color: #000;
						}
					}
					.colectBtnActive:hover {
						background: #F9B20E90;
						.icon {
							color: #fff;
						}
						.text {
							color: #000;
						}
					}
				}
				.item {
					padding: 0px 20px;
					margin: 0;
					display: flex;
					width: 100%;
					border-color: #44446D;
					border-width: 0 0 1px 0;
					align-items: center;
					border-style: solid;
					.lable {
						padding: 0 10px;
						color: #000000;
						white-space: nowrap;
						font-weight: 400;
						width: auto;
						font-size: 13px;
						line-height: 24px;
						text-align: right;
						height: auto;
					}
					.text {
						padding: 0 10px;
						color: #44446D;
						word-break: break-all;
						flex: 1;
						font-size: 14px;
						line-height: 24px;
						height: auto;
					}
					.price {
						color: #f00;
					}
					.bold {
						font-weight: bold;
					}
					.link {
						cursor: pointer;
						text-decoration: underline;
					}
				}
				.btn_box {
					padding: 10px 0;
					margin: 0 20px 20px 20px;
					display: flex;
					width: 100%;
					align-items: center;
					flex-wrap: wrap;
				}
				.el-input-number {
					margin: 0 0px 10px 0;
					display: block;
					width: 100%;
					position: relative;
					height: 60px;
					.el-input-number__decrease:hover:not(.is-disabled)~.el-input .el-input__inner:not(.is-disabled), .el-input-number__increase:hover:not(.is-disabled)~.el-input .el-input__inner:not(.is-disabled) {
					  border-color: none;
					}
					/deep/ .el-input-number__decrease {
						cursor: pointer;
						z-index: 1;
						display: flex;
						border-color: #DCDFE6;
						border-radius: 0;
						top: 1px;
						left: 1px;
						background: #44446D;
						width: 70px;
						justify-content: center;
						border-width: 0;
						align-items: center;
						position: absolute;
						border-style: solid;
						text-align: center;
						height: 60px;
					}
					
					/deep/ .el-input-number__decrease i {
						color: #fff;
						font-size: 14px;
					}
				
					/deep/ .el-input-number__increase {
						cursor: pointer;
						z-index: 1;
						display: flex;
						border-color: #DCDFE6;
						right: 1px;
						border-radius: 0;
						top: 1px;
						background: #44446D;
						width: 60px;
						justify-content: center;
						border-width: 0;
						align-items: center;
						position: absolute;
						border-style: solid;
						text-align: center;
						height: 60px;
					}
					
					/deep/ .el-input-number__increase i {
						color: #fff;
						font-size: 14px;
					}
					
					/deep/ .el-input .el-input__inner {
						border: 1px solid #DCDFE6;
						border-radius: 30px;
						padding: 0 40px;
						outline: none;
						color: #666;
						background: #FFFFFF;
						display: inline-block;
						width: 100%;
						font-size: 20px;
						line-height: 40px;
						text-align: center;
						height: 60px;
					}
				}
				.addCartBtn {
					border: 0;
					cursor: pointer;
					border-radius: 0;
					padding: 0 10px;
					margin: 0 5px 0 0;
					outline: none;
					color: #fff;
					background: #44446D;
					width: auto;
					font-size: 14px;
					line-height: 40px;
					height: 40px;
				}
				.addCartBtn:hover {
					opacity: 0.5;
				}
				.buyBtn {
					border: 0;
					cursor: pointer;
					border-radius: 0;
					padding: 0 10px;
					margin: 0 5px 0 0;
					outline: none;
					color: #fff;
					background: #54446D;
					width: auto;
					font-size: 14px;
					line-height: 40px;
					height: 40px;
				}
				.buyBtn:hover {
					opacity: 0.5;
				}
				.editBtn {
					border: 0;
					cursor: pointer;
					padding: 0 10px;
					margin: 0 5px 0 0;
					color: #fff;
					font-size: 14px;
					line-height: 40px;
					border-radius: 0;
					outline: none;
					background: #4D4462;
					width: auto;
					height: 40px;
					order: 6;
				}
				.editBtn:hover {
					opacity: 0.5;
				}
				.delBtn {
					border: 0;
					cursor: pointer;
					padding: 0 10px;
					margin: 0 5px 0 0;
					color: #fff;
					font-size: 14px;
					line-height: 40px;
					border-radius: 0;
					outline: none;
					background: #6B6B7A;
					width: auto;
					height: 40px;
					order: 7;
				}
				.delBtn:hover {
					opacity: 0.5;
				}
			}
		}
		.el-carousel {
			margin: 0 10px 0 0;
			width: calc(50% - 10px);
			height: 600px;
			/deep/ .el-carousel__indicator button {
				width: 0;
				height: 0;
				display: none;
			}
			/deep/ .el-carousel__container {
				.el-carousel__arrow--left {
					width: 36px;
					font-size: 12px;
					height: 36px;
				}
				.el-carousel__arrow--left:hover {
					background: red;
				}
				.el-carousel__arrow--right {
					width: 36px;
					font-size: 12px;
					height: 36px;
				}
				.el-carousel__arrow--right:hover {
					background: red;
				}
				.el-carousel__item {
					border-radius: 10px;
					width: 100%;
					height: 100%;
					img {
						object-fit: cover;
						width: 100%;
						height: 100%;
					}
				}
			}
		
			/deep/ .el-carousel__indicators {
				padding: 0;
				margin: 0;
				z-index: 2;
				position: absolute;
				list-style: none;
				li {
					padding: 0;
					margin: 0 4px;
					background: #fff;
					display: inline-block;
					width: 12px;
					opacity: 0.4;
					transition: 0.3s;
					height: 12px;
				}
				li:hover {
					padding: 0;
					margin: 0 4px;
					background: #fff;
					display: inline-block;
					width: 24px;
					opacity: 0.7;
					height: 12px;
				}
				li.is-active {
					padding: 0;
					margin: 0 4px;
					background: #fff;
					display: inline-block;
					width: 24px;
					opacity: 1;
					height: 12px;
				}
			}
		}
		.zancai {
			padding: 0;
			margin: 10px 0 20px;
			display: flex;
			width: 100%;
			justify-content: space-between;
			order: 3;
			height: auto;
			.zan {
				cursor: pointer;
				border-radius: 0;
				padding: 10px 0;
				margin: 0;
				background: #F5F5F5;
				display: flex;
				width: 40%;
				justify-content: center;
				align-items: center;
				.icon {
					margin: 0 3px;
					color: #ACACAC;
					font-size: 14px;
				}
				.text {
					margin: 0 3px;
					color: #ACACAC;
					font-size: 14px;
				}
			}
			.zan:hover {
				background: #BBB09B90;
				.icon {
					color: #fff;
				}
				.text {
					color: #fff;
				}
			}
			.zanActive {
				cursor: pointer;
				border-radius: 0;
				padding: 10px 0;
				margin: 0;
				background: #BBB09B;
				flex: 1;
				display: flex;
				width: 40%;
				justify-content: center;
				align-items: center;
				.icon {
					color: #fff;
				}
				.text {
					color: #fff;
				}
			}
			.zanActive:hover {
				background: #BBB09B90;
				.icon {
					color: #fff;
				}
				.text {
					color: #fff;
				}
			}
			
			.cai {
				cursor: pointer;
				padding: 10px 0;
				margin: 0;
				background: #CCDAF1;
				display: flex;
				width: 40%;
				justify-content: center;
				align-items: center;
				.icon {
					margin: 0 3px;
					color: #44446D;
					font-size: 14px;
				}
				.text {
					margin: 0 3px;
					color: #44446D;
					font-size: 14px;
				}
			}
			.cai:hover {
				background: #C4C2BF90;
				.icon {
					color: #fff;
				}
				.text {
					color: #fff;
				}
			}
			.caiActive {
				cursor: pointer;
				padding: 10px 0;
				margin: 0;
				background: #C4C2BF;
				flex: 1;
				display: flex;
				width: 40%;
				justify-content: center;
				align-items: center;
				.icon {
					color: #fff;
				}
				.text {
					color: #fff;
				}
			}
			.caiActive:hover {
				background: #C4C2BF90;
				.icon {
					color: #fff;
				}
				.text {
					color: #fff;
				}
			}
		}
		.detail-tabs {
			border: 2px solid #44446D;
			border-radius: 0;
			margin: 20px 0 0 0 ;
			color: #6E6E6E;
			background: #CCDAF1;
			width: 100%;
			order: 5;
			& /deep/ .el-tabs__header .el-tabs__nav-wrap {
				margin-bottom: 0;
			}
			/deep/ .el-tabs__header {
				border-radius: 0px 0px 20px 20px;
				padding: 15px 10px;
				margin: 0;
				background: #FFD99D;
			}
			
			/deep/ .el-tabs__header .el-tabs__item {
				border: 0;
				padding: 0 20px 0 10px ;
				margin: 0 10px;
				color: #44446D;
				font-weight: 500;
				display: inline-block;
				font-size: 14px;
				line-height: 40px;
				background: #EDF0FA;
				width: 100px;
				position: relative;
				list-style: none;
				text-align: center;
				height: 40px;
			}
			
			/deep/ .el-tabs__header .el-tabs__item:hover {
				border: 0;
				padding: 0 20px 0 10px ;
				margin: 0 10px;
				background-size: 100% 100%;
				color: #fff;
				background: #44446D;
				width: 100px;
				text-align: center;
			}
			
			/deep/ .el-tabs__header .el-tabs__item.is-active {
				border: 0;
				padding: 0 20px 0 10px ;
				margin: 0 10px;
				background-size: 100% 100%;
				color: #fff;
				background: #44446D;
				width: 100px;
				text-align: center;
			}
			
			/deep/ .el-tabs__content {
				padding: 15px;
			}
			.commentForm {
				border: 1px solid #44446D;
				margin: 0 0 20px;
				.item {
					padding: 10px;
					display: flex;
					width: 100%;
					height: auto;
					/deep/ .el-form-item__label {
						padding: 0 10px 0 0;
						color: #666;
						width: 80px;
						font-size: 14px;
						line-height: 40px;
						text-align: right;
					}
					.editor {
						border: 1px solid #44446D;
						border-radius: 4px;
						outline: none;
						color: #333;
						width: 100%;
						font-size: 14px;
						min-height: 400px;
						line-height: 32px;
						/deep/ .avatar-uploader {
							height: 0;
							line-height: 0;
						}
					}
				}
				.commentBtn {
					padding: 0 0 0 80px;
					margin: 10px 0 0;
					display: flex;
					width: 100%;
					justify-content: flex-end;
					height: auto;
					.submitBtn {
						border: 0;
						cursor: pointer;
						border-radius: 0;
						padding: 0;
						margin: 0 20px 10px 0;
						outline: none;
						color: rgba(255, 255, 255, 1);
						background: #000000;
						width: 128px;
						font-size: 14px;
						line-height: 40px;
						height: 40px;
					}
					.submitBtn:hover {
						background: rgba(64, 158, 255, 0.5);
					}
					.resetBtn {
						border: 0;
						cursor: pointer;
						border-radius: 0;
						padding: 0;
						margin: 0 20px 10px 0;
						outline: none;
						color: #6E6E6E;
						background: #C0C0C0;
						width: 128px;
						font-size: 14px;
						line-height: 40px;
						height: 40px;
					}
					.resetBtn:hover {
						background: rgba(64, 158, 255, 0.5);
					}
				}
			}
			.comment-list {
				border: 2px solid #44446D;
				border-radius: 30px 30px 30px 0px;
				padding: 15px 20px;
				.comment-item {
					padding: 8px 0;
					margin: 0 0 20px;
					width: 100%;
					border-color: #44446D;
					border-width: 0 0 1px 0;
					align-items: center;
					position: relative;
					border-style: solid;
					height: auto;
					.istop {
						top: 0;
						background: none;
						position: absolute;
						right: 50%;
						.icon {
							color: #BBB09B;
							font-weight: bold;
						}
					}
					.user {
						display: flex;
						width: 100%;
						align-items: center;
						height: auto;
						.el-image {
							border-radius: 100%;
							margin: 0 10px 0 0;
							object-fit: cover;
							width: 40px;
							height: 40px;
						}
						.name {
							color: #333;
							font-size: 16px;
						}
					}
					.comment-time {
						color: #666;
					}
					.comment-content-box {
						border-radius: 4px;
						padding: 8px;
						margin: 10px 0px 0px;
						word-wrap: break-word;
						color: #6F6F6F;
						font-size: 14px;
						line-height: 30px;
						.zancai-box {
							margin: 0 20px;
							display: flex;
							align-items: center;
							height: 30px;
							.zan-item {
								color: #6F6F6F;
								display: flex;
								align-items: center;
								.icon {
								color: inherit;
								font-size: 14px;
								}
								.label {
								display: none;
								font-size: 14px;
								}
								.num {
								color: inherit;
								font-size: 14px;
								}
							}
							.zan-item.active {
								background: none;
								.icon {
								color: #44446D;
								font-size: 14px;
								}
								.label {
								color: #44446D;
								display: none;
								font-size: 14px;
								}
								.num {
								color: #44446D;
								font-size: 14px;
								}
							}
							.zan-item:hover {
								opacity: 0.8;
								.icon {
								color: #44446D;
								}
								.label {
								color: #44446D;
								}
								.num {
								color: #44446D;
								}
							}
							.cai-item {
								display: flex;
								align-items: center;
								.icon {
								font-size: 14px;
								}
								.label {
								display: none;
								font-size: 14px;
								}
								.num {
								font-size: 14px;
								}
							}
							.cai-item.active {
								background: none;
								.icon {
								color: #44446D;
								font-size: 14px;
								}
								.label {
								color: #44446D;
								display: none;
								font-size: 14px;
								}
								.num {
								color: #44446D;
								font-size: 14px;
								}
							}
							.cai-item:hover {
								opacity: 0.8;
								.icon {
								color: #44446D;
								}
								.label {
								color: #44446D;
								}
								.num {
								color: #44446D;
								}
							}
						}
						.comment-btn {
							margin: 0;
							top: 15px;
							display: flex;
							width: 100%;
							justify-content: flex-end;
							align-items: center;
							position: absolute;
							right: 15px;
							height: auto;
							.delBtn {
								border: 0;
								cursor: pointer;
								border-radius: 0;
								padding: 0 20px;
								margin: 0 0 0 10px;
								outline: none;
								color: rgba(255, 255, 255, 1);
								background: #000;
								width: auto;
								font-size: 14px;
								line-height: 30px;
								height: 30px;
							}
						}
					}
				}
			}
		}
	}
	.share_view{
		box-shadow: 0 1px 6px rgba(0,0,0,.3);
		z-index: 11;
		bottom: 20%;
		background: #fff;
		position: fixed;
		right: 0;
		.share:last-of-type{
			border:none;
		}
	}
</style>
