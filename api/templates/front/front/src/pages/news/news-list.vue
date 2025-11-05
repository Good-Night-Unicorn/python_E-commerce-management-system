<template>
	<div>
		<div class="breadcrumb-preview">
			<el-breadcrumb :separator="''">
				<el-breadcrumb-item class="item1" to="/"><a>首页</a></el-breadcrumb-item>
				<el-breadcrumb-item class="item2" v-for="(item, index) in breadcrumbItem" :key="index"><a>{{item.name}}</a></el-breadcrumb-item>
			</el-breadcrumb>
		</div>
	
		<div class="news-preview-pv">
			<el-form :inline="true" :model="formSearch" class="list-form-pv">
				<el-form-item class="search-item">
					<el-input v-model="title" placeholder="标题"></el-input>
				</el-form-item>
				<el-button class="search-btn" type="primary" @click="getNewsList(1)">
					<span class="icon iconfont icon-chakan14"></span>
					搜索
				</el-button>
			</el-form>
			
			<!-- category -->
			<div class="category-list">
				<div class="item" @click="categoryClick(0)" :class="categoryIndex == 0 ? 'active' : ''">全部</div>
				<div v-for="(item,index) in categoryList" @click="categoryClick(index+1)" :key="index" class="item" :class="categoryIndex == index+1 ? 'active' : ''">{{item.typename}}</div>
			</div>
			<!-- 样式三 -->
			<div class="list3 index-pv1">
				<div v-for="item in newsList" :key="item.id" @click="toNewsDetail(item)" class="list-item animation-box">
					<div class="name">{{item.title}}</div>
					<div class="desc">{{item.introduction}}</div>
					<div class="time_item">
						<span class="icon iconfont icon-shijian21"></span>
						<span class="label">发布时间：</span>
						<span class="text">{{item.addtime}}</span>
					</div>
					<div class="publisher_item">
						<span class="icon iconfont icon-geren16"></span>
						<span class="label">发布人：</span>
						<span class="text">{{item.name}}</span>
					</div>
					<div class="like_item">
						<span class="icon iconfont icon-zan10"></span>
						<span class="label">点赞数：</span>
						<span class="text">{{item.thumbsupnum}}</span>
					</div>
					<div class="collect_item">
						<span class="icon iconfont icon-shoucang10"></span>
						<span class="label">收藏量：</span>
						<span class="text">{{item.storeupnum}}</span>
					</div>
					<div class="view_item">
						<span class="icon iconfont icon-chakan9"></span>
						<span class="label">点击量：</span>
						<span class="text">{{item.clicknum}}</span>
					</div>
					<div class="tags">新闻动态</div>
				</div>
			</div>
		
			<el-pagination
				background
				id="pagination" class="pagination"
				:pager-count="7"
				:page-size="pageSize"
				:page-sizes="pageSizes"
				prev-text="上一页"
				next-text="下一页"
				:hide-on-single-page="true"
				:layout='["total","prev","pager","next"].join()'
				:total="total"
				@current-change="curChange"
				@size-change="sizeChange"
				@prev-click="prevClick"
				@next-click="nextClick"
				></el-pagination>

			<!-- 热门信息 -->
			<div class="hot">
				<div class="hot-title">热门信息</div>
				<div class="hot-list">
					<div class="hot-item" v-for="item in hotList" :key="item.id" @click="toNewsDetail(item)">
						<img :src="baseUrl + item.picture" alt="">
						<div class="hot-name">{{ item.title }}</div>
						<div class="hot-time">{{item.addtime}}</div>
					</div>
				</div>
			</div>
			<!-- 最新动态 -->
			<div class="news">
				<div class="news-title">最新动态</div>
				<div class="news-list">
					<div class="news-item" v-for="item in recommendList" :key="item.id" @click="toNewsDetail(item)">
						<img :src="baseUrl + item.picture" alt="">
						<div class="news-name">{{ item.title }}</div>
						<div class="news-time">{{item.addtime}}</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	export default {
		//数据集合
		data() {
			return {
				baseUrl: this.$config.baseUrl,
				breadcrumbItem: [
				  {
					name: '系统公告'
				  }
				],
				newsList: [],
				total: 1,
				pageSize: 10,
				pageSizes: [],
				totalPage: 1,
				layouts: '',
				title: '',
				categoryIndex: 0,
				categoryList: [],
				hotList: [],
				recommendList: [],
			}
		},
		created() {
			this.getCategoryList()
			
			this.getHotList()
			this.getRecommendList()
		},
		watch:{
			$route(newValue){
				this.getCategoryList()
			}
		},
		//方法集合
		methods: {
			getCategoryList(){
				this.$http.get('newstype/list', {params: {sort: 'typename',order: 'desc'}}).then(res => {
					if (res.data.code == 0) {
						this.categoryList = res.data.data.list;
						if(this.$route.query.homeFenlei){
							for(let i=0;i<this.categoryList.length;i++) {
								if(this.$route.query.homeFenlei == this.categoryList[i].typename) {
									this.categoryIndex = i + 1;
									const currentRoute = this.$route;
									const routeWithoutQuery = { ...currentRoute };
									delete routeWithoutQuery.query;
									this.$router.replace(routeWithoutQuery)
									break;
								}
							}
						}
						this.getNewsList(1);
					}
				});
			},
			categoryClick(index) {
				this.categoryIndex = index
				this.getNewsList()
			},
			getNewsList(page) {
				let params = {page, limit: this.pageSize,sort:'addtime',order:'desc'};
				let searchWhere = {};
				if(this.title != '') searchWhere.title = '%' + this.title + '%';
				if(this.categoryIndex!=0){
					searchWhere.typename = this.categoryList[this.categoryIndex - 1].typename
				}
				this.$http.get('news/list', {params: Object.assign(params, searchWhere)}).then(res => {
					if (res.data.code == 0) {
						this.newsList = res.data.data.list;
						this.total = res.data.data.total;
						this.pageSize = Number(res.data.data.pageSize);
						this.totalPage = res.data.data.totalPage;
						if(this.pageSizes.length==0){
							this.pageSizes = [this.pageSize, this.pageSize*2, this.pageSize*3, this.pageSize*5];
						}
					}
				});
			},
			getHotList(){
				let params = {page:1, limit: 4,sort:'addtime',order:'desc'};
				this.$http.get('news/autoSort', {params: params}).then(res => {
					if (res.data.code == 0) {
						this.hotList = res.data.data.list;
					}
				});
			},
			getRecommendList(){
				let url = 'news/autoSort'
				if(localStorage.getItem('frontToken')){
					url = 'news/autoSort2'
				}
				let params = {page:1, limit: 4,sort:'addtime',order:'desc'};
				this.$http.get(url, {params: params}).then(res => {
					if (res.data.code == 0) {
						this.recommendList = res.data.data.list;
					}
				});
			},
			curChange(page) {
				this.getNewsList(page);
			},
			sizeChange(size){
				this.pageSize = size
				this.getNewsList(1);
			},
			prevClick(page) {
				this.getNewsList(page);
			},
			nextClick(page) {
				this.getNewsList(page);
			},
			toNewsDetail(item) {
				this.$router.push({path: '/index/newsDetail', query: {id: item.id}});
			}
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.news-preview-pv {
				padding: 30px calc((100% - 1200px)/2);
				margin: 0;
				flex-direction: column;
				background: #EDF0FA;
				display: flex;
				width: 100%;
				align-items: center;
				position: relative;
				.list-form-pv {
						border-radius: 30px;
						padding: 0;
						margin: 0 0 20px;
						background: #fff;
						display: flex;
						width: auto;
						border-width: 4px 0 0;
						justify-content: center;
						align-items: center;
						flex-wrap: wrap;
						height: auto;
						.search-item {
								margin: 0 10px;
								.el-input {
										width: 100%;
									}
				.el-input /deep/ .el-input__inner {
										border: 0;
										border-radius: 8px;
										padding: 0 10px;
										margin: 0;
										outline: none;
										color: #333;
										width: 300px;
										font-size: 14px;
										line-height: 42px;
										height: 42px;
									}
			}
			.search-btn {
								cursor: pointer;
								border: 0;
								border-radius: 30px;
								padding: 0px 15px;
								margin: 0;
								outline: none;
								color: #fff;
								background: #44446D;
								width: auto;
								font-size: 14px;
								line-height: 42px;
								height: 42px;
								.icon {
										margin: 0 10px 0 0;
										color: #fff;
										font-size: 14px;
									}
			}
		}
		.category-list {
						border-radius: 0 0 20px 20px;
						padding: 0 10px ;
						margin: 0 0 20px;
						background: #FFD99D;
						display: flex;
						width: 100%;
						overflow-x: scroll;
						height: auto;
						.item {
								cursor: pointer;
								border-radius: 0;
								padding: 0 15px;
								max-height: 40px;
								margin: 10px 30px 10px 20px;
								color: #44446D;
								background: #EDF0FA;
								display: flex;
								min-height: 40px;
								justify-content: center;
								align-items: center;
								min-width: 150px;
							}
			
			.item:hover {
								color: #fff;
								background: #44446D;
								text-align: center;
							}
			
			.item.active {
								color: #fff;
								background: #44446D;
								text-align: center;
							}
		}
		.list3 {
						display: flex;
						width: 100%;
						flex-wrap: wrap;
						height: auto;
						.list-item {
								border: 1px solid #44446D;
								padding: 10px;
								margin: 0 10px 10px 10px;
								background: #CCDAF1;
								width: calc(50% - 20px);
								position: relative;
								height: auto;
								.name {
										color: #000000;
										font-size: 14px;
										line-height: 32px;
									}
				.desc {
										color: #555555;
										font-size: 14px;
										line-height: 21px;
									}
				.time_item {
										padding: 0;
										display: inline-block;
										.icon {
												margin: 0 2px 0 0;
												color: #44446D;
												font-size: 12px;
												line-height: 1.5;
											}
					.label {
												color: #44446D;
												font-size: 12px;
												line-height: 1.5;
											}
					.text {
												color: #44446D;
												font-size: 12px;
												line-height: 1.5;
											}
				}
				.publisher_item {
										padding: 0 10px;
										display: inline-block;
										.icon {
												margin: 0 2px 0 0;
												color: #5E70C7;
												font-size: 12px;
												line-height: 1.5;
											}
					.label {
												color: #5E70C7;
												font-size: 12px;
												line-height: 1.5;
											}
					.text {
												color: #5E70C7;
												font-size: 12px;
												line-height: 1.5;
											}
				}
				.like_item {
										padding: 0 10px;
										display: inline-block;
										.icon {
												margin: 0 2px 0 0;
												color: #7D7DD4;
												font-size: 12px;
												line-height: 1.5;
											}
					.label {
												color: #7D7DD4;
												font-size: 12px;
												line-height: 1.5;
											}
					.text {
												color: #7D7DD4;
												font-size: 12px;
												line-height: 1.5;
											}
				}
				.collect_item {
										padding: 0 10px;
										display: inline-block;
										.icon {
												margin: 0 2px 0 0;
												color: #2222AA;
												font-size: 12px;
												line-height: 1.5;
											}
					.label {
												color: #2222AA;
												font-size: 12px;
												line-height: 1.5;
											}
					.text {
												color: #2222AA;
												font-size: 12px;
												line-height: 1.5;
											}
				}
				.view_item {
										padding: 0 10px 0 0;
										display: inline-block;
										.icon {
												margin: 0 2px 0 0;
												color: #7D7DD4;
												font-size: 12px;
												line-height: 1.5;
											}
					.label {
												color: #7D7DD4;
												font-size: 12px;
												line-height: 1.5;
											}
					.text {
												color: #7D7DD4;
												font-size: 12px;
												line-height: 1.5;
											}
				}
				.tags {
										padding: 0 10px;
										margin: 10px 0 0 0;
										color: #fff;
										background: #44446D;
										display: block;
										width: 80px;
										font-size: 14px;
										line-height: 32px;
										text-align: center;
									}
			}
		}
		.hot {
						margin: 0 0 20px;
						width: 100%;
						height: auto;
						.hot-title {
								padding: 0  165px;
								margin: 0px auto 20px ;
								flex-direction: column;
								color: #44446D;
								background: url(http://codegen.caihongy.cn/20250118/8fc0638edcbd47b4bdaa28e8495ba36b.png) no-repeat center center / 100% 100%;
								display: flex;
								width: 1200px;
								font-size: 32px;
								line-height: 100px;
								justify-content: flex-end;
								text-align: left;
								height: 100px;
							}
			.hot-list {
								border-radius: 30px;
								padding: 0;
								display: flex;
								width: 100%;
								flex-wrap: wrap;
								height: auto;
								.hot-item {
										border: 1px solid #44446D;
										border-radius: 30px 30px 0px 30px;
										padding: 10px 10px 20px 10px;
										margin: 0 1%;
										background: #CCDAF3;
										width: 23%;
										height: auto;
										img {
												border-radius: 20px;
												margin: 10px;
												object-fit: cover;
												display: block;
												width: calc(100% - 20px);
												border-color: #BBB09B;
												border-width: 0;
												border-style: solid;
												height: 150px;
											}
					.hot-name {
												padding: 4px 5px 0;
												color: #44446D;
												font-weight: 400;
												width: 100%;
												font-size: 16px;
												line-height: 1.5;
												text-align: center;
											}
					.hot-time {
												padding: 0 5px;
												color: #9e9e9e;
												display: none;
												font-size: 12px;
												line-height: 1.5;
												text-align: right;
											}
				}
			}
		}
		.news {
						margin: 0 0 20px;
						width: 100%;
						height: auto;
						.news-title {
								padding: 0  165px;
								margin: 0px auto 20px ;
								flex-direction: column;
								color: #44446D;
								background: url(http://codegen.caihongy.cn/20250118/8fc0638edcbd47b4bdaa28e8495ba36b.png) no-repeat center center / 100% 100%;
								display: flex;
								width: 1200px;
								font-size: 32px;
								line-height: 100px;
								justify-content: flex-end;
								text-align: left;
								height: 100px;
							}
			.news-list {
								border-radius: 30px;
								display: flex;
								width: 100%;
								flex-wrap: wrap;
								height: auto;
								.news-item {
										border: 1px solid #44446D;
										border-radius: 30px 30px 0px 30px;
										padding: 10px 10px 20px 10px;
										margin: 0 1%;
										background: #CCDAF3;
										width: 23%;
										height: auto;
										img {
												border-radius: 20px;
												margin: 10px;
												object-fit: cover;
												display: block;
												width: calc(100% - 20px);
												border-color: #BBB09B;
												border-width: 0;
												border-style: solid;
												height: 150px;
											}
					.news-name {
												padding: 4px 5px 0;
												color: #44446D;
												font-weight: 400;
												width: 100%;
												font-size: 16px;
												line-height: 1.5;
												text-align: center;
											}
					.news-time {
												padding: 0 10px;
												color: #999;
												display: none;
												font-size: 14px;
												line-height: 12px;
												text-align: right;
											}
				}
			}
		}
	}
	
	.index-pv1 .animation-box {
		transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
		z-index: initial;
	}
	
	.index-pv1 .animation-box:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				background: linear-gradient( 357deg, #F3EFE7 0%, #FFFFFF 100%);
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
	}
	
	.index-pv1 .animation-box img {
		transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
	}
	
	.index-pv1 .animation-box img:hover {
				transform: rotate(0deg) scale(0.9) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
</style>
