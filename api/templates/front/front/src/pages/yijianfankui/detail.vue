<template>
	<div>
	<!--  -->
		<div class="breadcrumb-preview">
			<el-breadcrumb :separator="''">
				<el-breadcrumb-item class="item1" to="/"><a>首页</a></el-breadcrumb-item>
				<el-breadcrumb-item class="item2" v-for="(item, index) in breadcrumbItem" :key="index" :to="'/index/yijianfankui?centerType=' + (centerType?'1':'0')"><a>{{item.name}}</a></el-breadcrumb-item>
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
							{{detail.biaoti}}
						</div>
					</div>
					<div class="item">
						<div class="lable">反馈时间</div>
						<div class="text "  >{{detail.fankuishijian}}</div>
					</div>
					<div class="item">
						<div class="lable">用户账号</div>
						<div class="text "  >{{detail.yonghuzhanghao}}</div>
					</div>
					<div class="item">
						<div class="lable">用户姓名</div>
						<div class="text "  >{{detail.yonghuxingming}}</div>
					</div>
					<div class="item" v-if="centerType">
						<div class="lable">回复内容</div>
						<div class="text">{{detail.shhf}}</div>
					</div>
					<div class="btn_box">
						<el-button class="editBtn" v-if="btnAuth('yijianfankui','修改')" @click="editClick">修改</el-button>
						<el-button class="delBtn" v-if="btnAuth('yijianfankui','删除')" @click="delClick">删除</el-button>
						<el-button class="auditBtn" v-if="btnAuth('yijianfankui','审核')" @click="onSH" type="warning">回复</el-button>
					</div>
				</div>
			</div>
		
			<el-carousel v-if="detailBanner.length" trigger="click" indicator-position="inside" arrow="always" type="default" direction="horizontal" height="600px" :autoplay="false" :interval="3000" :loop="true">
				<el-carousel-item v-for="item in detailBanner" :key="item.id">
					<img :preview-src-list="[item]" v-if="item.substr(0,4)=='http'" :src="item" class="image">
					<img :preview-src-list="[baseUrl + item]" v-else :src="baseUrl + item" class="image">
				</el-carousel-item>
			</el-carousel>


		

			<el-tabs class="detail-tabs" v-model="activeName" type="border-card" v-if="tabsNum>0" >
				<el-tab-pane label="意见反馈" name="first">
					<div class="ql-snow ql-editor" v-html="detail.yijianfankui"></div>
				</el-tab-pane>
			</el-tabs>
			<el-dialog title="回复" :visible.sync="sfshVisiable" width="50%">
				<el-form ref="form" :model="form" label-width="80px">
					<el-form-item label="内容">
						<el-input type="textarea" :rows="8" v-model="shForm.shhf"></el-input>
					</el-form-item>
				</el-form>
				<span slot="footer" class="dialog-footer">
					<el-button @click="sfshVisiable = false">取 消</el-button>
					<el-button type="primary" @click="shHandler">确 定</el-button>
				</span>
			</el-dialog>

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
				tablename: 'yijianfankui',
				baseUrl: '',
				breadcrumbItem: [
					{
						name: '意见反馈'
					}
				],
				title: '',
				detailBanner: [],
				userid: Number(localStorage.getItem('frontUserid')),
				id: 0,
				detail: {},
				tabsNum: 1,
				activeName: 'first',
				total: 1,
				pageSize: 10,
				totalPage: 1,
				buynumber: 1,
				sfshVisiable: false,
				shForm: {
					sfsh: '是',
					shhf: ''
				},
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
						this.title = this.detail.biaoti;
						if(this.detail.fengmian) {
							this.detailBanner = this.detail.fengmian.split(",w").length>1?[this.detail.fengmian]:this.detail.fengmian.split(',');
						}
						this.$forceUpdate();
						if(localStorage.getItem('frontToken')){
						}

					}
				});
			},
			onSH() {
				this.sfshVisiable = true;
			},
			shHandler(){
				this.$confirm(`确定操作?`, "提示", {
					confirmButtonText: "确定",
					cancelButtonText: "取消",
					type: "warning"
				}).then(() => {
					this.detail.shhf = this.shForm.shhf;
					this.$http.post(`${this.tablename}/update`, this.detail).then(res => {
						if (res.data.code == 0) {
							this.sfshVisiable = false;
							this.$message({
								message: "操作成功",
								type: "success",
								duration: 1500,
							});
						}
					});
				});
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
					this.$router.push({path: '/index/yijianfankui', query: params});
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
				this.$router.push(`/index/yijianfankuiAdd?type=edit&&id=${this.detail.id}`);
			},
			// 删除
			async delClick(){
				await this.$confirm('是否删除此意见反馈？') .then(_ => {
					this.$http.post('yijianfankui/delete', [this.detail.id]).then(async res => {
						if (res.data.code == 0) {
							this.$message({
								type: 'success',
								message: '删除成功!',
								duration: 1500,
								onClose: () => {
									history.back()
								}
							});
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
				.auditBtn {
					border: 0;
					cursor: pointer;
					border-radius: 0;
					padding: 0 10px;
					margin: 0 5px 0 0;
					outline: none;
					color: #fff;
					background: #503A70;
					width: auto;
					font-size: 14px;
					line-height: 40px;
					height: 40px;
				}
				.auditBtn:hover {
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
