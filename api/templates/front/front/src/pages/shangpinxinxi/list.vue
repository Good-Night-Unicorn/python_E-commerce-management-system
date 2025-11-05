<template>
	<div>
		<div class="breadcrumb-preview">
			<el-breadcrumb :separator="''">
				<el-breadcrumb-item class="item1" to="/"><a>首页</a></el-breadcrumb-item>
				<el-breadcrumb-item class="item2" v-for="(item, index) in breadcrumbItem" :key="index"><a>{{item.name}}</a></el-breadcrumb-item>
			</el-breadcrumb>
		</div>
		<div v-if="centerType" class="back_box">
			<el-button class="backBtn" size="mini" @click="backClick">
				<span class="icon iconfont icon-jiantou33"></span>
				<span class="text">返回</span>
			</el-button>
		</div>
		<div class="list-preview">
			<el-form :inline="true" :model="formSearch" class="list-form-pv">
				<el-form-item class="list-item">
					<div class="lable">商品名称：</div>
					<el-input v-model="formSearch.shangpinmingcheng" placeholder="商品名称" @keydown.enter.native="getList(1, curFenlei)" clearable></el-input>
				</el-form-item>
				<el-form-item class="list-item">
					<div class="lable">价格：</div>
					<el-input v-model="formSearch.pricestart" placeholder="最小价格" clearable></el-input>
				</el-form-item>
				<el-form-item class="list-item">
					<el-input v-model="formSearch.priceend" placeholder="最大价格" clearable></el-input>
				</el-form-item>
				<el-button class="list-search-btn" v-if=" true " type="primary" @click="getList(1, curFenlei)">
					<i class="el-icon-search"></i>
					查询
				</el-button>
				<el-button class="list-add-btn" v-if="btnAuth('shangpinxinxi','新增')" type="primary" @click="add('/index/shangpinxinxiAdd')">
					<i class="el-icon-circle-plus-outline"></i>
					添加
				</el-button>
			</el-form>
			<div class="select2">
				<div class="select2-list" v-for="(item,index) in selectOptionsList" :key="index">
					<div class="label">{{item.name}}：</div>
					<div class="item-body">
						<div class="item" @click="selectClick2(item,-1)" :class="item.check ==-1 ? 'active' : ''">全部</div>
						<div class="item" @click="selectClick2(item,index1)" :class="item.check == index1 ? 'active' : ''" v-for="item1,index1 in item.list" :key="index1">{{item1}}</div>
					</div>
				</div>
			</div>
			<div class="sort_view">
				<el-button class="price-sort-btn" @click="sortClick('price')">
					<span class="icon iconfont icon-zhifudingjin" v-if="sortType!='price'"></span>
					<span class="icon iconfont icon-jiantou23" v-else-if="sortType=='price'&&sortOrder=='desc'"></span>
					<span class="icon iconfont icon-jiantou24" v-else-if="sortType=='price'&&sortOrder=='asc'"></span>
					<span class="text">价格</span>
				</el-button>
				<el-button class="click-sort-btn" @click="sortClick('clicknum')">
					<span class="icon iconfont icon-liulan12" v-if="sortType!='clicknum'"></span>
					<span class="icon iconfont icon-jiantou23" v-else-if="sortType=='clicknum'&&sortOrder=='desc'"></span>
					<span class="icon iconfont icon-jiantou24" v-else-if="sortType=='clicknum'&&sortOrder=='asc'"></span>
					<span class="text">点击量：</span>
				</el-button>
				<el-button class="collect-sort-btn" @click="sortClick('storeupnum')">
					<span class="icon iconfont icon-shoucang12" v-if="sortType!='storeupnum'"></span>
					<span class="icon iconfont icon-jiantou23" v-else-if="sortType=='storeupnum'&&sortOrder=='desc'"></span>
					<span class="icon iconfont icon-jiantou24" v-else-if="sortType=='storeupnum'&&sortOrder=='asc'"></span>
					<span class="text">收藏数</span>
				</el-button>
				<el-button class="like-sort-btn" @click="sortClick('thumbsupnum')">
					<span class="icon iconfont icon-zan10" v-if="sortType!='thumbsupnum'"></span>
					<span class="icon iconfont icon-jiantou23" v-else-if="sortType=='thumbsupnum'&&sortOrder=='desc'"></span>
					<span class="icon iconfont icon-jiantou24" v-else-if="sortType=='thumbsupnum'&&sortOrder=='asc'"></span>
					<span class="text">点赞数</span>
				</el-button>
			</div>
			<div class="list">
				<!-- 样式三 -->
				<div class="list3 index-pv1">
					<div v-for="(item, index) in dataList" :key="index" @click.stop="toDetail(item)" class="list-item animation-box">
						<div class="img">
							<img @click.stop="imgPreView(item.tupian)" v-if="item.tupian && item.tupian.substr(0,4)=='http'&&item.tupian.split(',w').length>1" :src="item.tupian" class="image" />
							<img @click.stop="imgPreView(item.tupian.split(',')[0])" v-else-if="item.tupian && item.tupian.substr(0,4)=='http'" :src="item.tupian.split(',')[0]" class="image" />
							<img @click.stop="imgPreView(baseUrl + (item.tupian?item.tupian.split(',')[0]:''))" v-else :src="baseUrl + (item.tupian?item.tupian.split(',')[0]:'')" class="image" />
						</div>
						<div class="item-info">
							<div>
								<div class="name">{{item.shangpinmingcheng}}</div>
								<div class="price"><span style="font-size: 12px">￥</span>{{item.price}}</div>
								<div class="time_item">
									<span class="icon iconfont icon-shijian21"></span>
									<span class="label">发布时间：</span>
									<span class="text">{{item.addtime.split(' ')[0]}}</span>
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
							</div>
							<div class="desc ql-snow ql-editor" v-html="item.shangpinjieshao"></div>
						</div>
					</div>
				</div>
			</div>

	
			<el-pagination
				background
				id="pagination"
				class="pagination"
				:pager-count="7"
				:page-size="pageSize"
				prev-text="上一页"
				next-text="下一页"
				:hide-on-single-page="true"
				:layout='["total","prev","pager","next"].join()'
				:total="total"
				:page-sizes="pageSizes"
				@current-change="curChange"
				@size-change="sizeChange"
				@prev-click="prevClick"
				@next-click="nextClick"
				></el-pagination>
		</div>
		<el-dialog title="预览图" :visible.sync="previewVisible" width="50%">
			<img :src="previewImg" alt="" style="width: 100%;">
		</el-dialog>
	</div>
</template>
<script>
	export default {
		//数据集合
		data() {
			return {
				selectIndex2: 0,
				selectOptionsList: [],
				layouts: '',
				swiperIndex: -1,
				baseUrl: '',
				breadcrumbItem: [
					{
						name: '商品信息'
					}
				],
				formSearch: {
					shangpinmingcheng: '',
					shangpinleixing: '',
					price: '',
				},
				fenlei: [],
				feileiColumn: '',
				dataList: [],
				total: 1,
				pageSize: 12,
				pageSizes: [],
				totalPage: 1,
				curFenlei: '全部',
				isPlain: false,
				indexQueryCondition: '',
				shangpinleixingOptions: [],
				timeRange: [],
				centerType:false,
				previewImg: '',
				previewVisible: false,
				sortType: 'id',
				sortOrder: 'desc',
			}
		},
		async created() {
			if(this.$route.query.centerType&&this.$route.query.centerType!=0){
				this.centerType = true
			}
			this.baseUrl = this.$config.baseUrl;
			await this.$http.get('option/shangpinleixing/shangpinleixing').then(res => {
				if (res.data.code == 0) {
					this.shangpinleixingOptions = res.data.data;
					this.selectOptionsList.push({name:'商品类型',list:this.shangpinleixingOptions,tableName: 'shangpinleixing',check: -1})
				}
			});
			await this.getFenlei();
			let fenlei = '全部'
			if(this.$route.query.homeFenlei){
				fenlei = this.$route.query.homeFenlei
			}
			this.getList(1, fenlei);
		},
		watch:{
			$route(newValue){
				this.getList(1, newValue.query.homeFenlei);
			}
		},
		//方法集合
		methods: {
			selectClick2(row,index) {
				row.check = index
				if(index == -1){
					this.formSearch[row.tableName] = ''
				}else {
					this.formSearch[row.tableName] = row.list[index]
				}
				this.getList()
			},
			add(path) {
				let query = {}
				if(this.centerType){
					query.centerType = 1
				}
				this.$router.push({path: path,query:query});
			},
			async getFenlei() {
			},
			getList(page, fenlei, ref = '') {
				let params = {
					page,
					limit: this.pageSize,
					onshelves: 1
				};
				let searchWhere = {};
				if (this.formSearch.shangpinmingcheng != '') searchWhere.shangpinmingcheng = '%' + this.formSearch.shangpinmingcheng + '%';
				if (this.formSearch.shangpinleixing != '') searchWhere.shangpinleixing = this.formSearch.shangpinleixing;
				if(this.formSearch.pricestart!='' && this.formSearch.pricestart!=undefined ){
					searchWhere.pricestart = this.formSearch.pricestart
				}
				if(this.formSearch.priceend!='' && this.formSearch.priceend!=undefined){
					searchWhere.priceend = this.formSearch.priceend
				}
				let user = JSON.parse(localStorage.getItem('sessionForm'))
				if (this.sortType) searchWhere.sort = this.sortType
				if (this.sortOrder) searchWhere.order = this.sortOrder
				this.$http.get(`shangpinxinxi/${this.centerType?'page':'list'}`, {params: Object.assign(params, searchWhere)}).then(res => {
					if (res.data.code == 0) {
						this.dataList = res.data.data.list;
						this.total = Number(res.data.data.total);
						this.pageSize = Number(res.data.data.pageSize);
						this.totalPage = res.data.data.totalPage;
						if(this.pageSizes.length==0){
							this.pageSizes = [this.pageSize, this.pageSize*2, this.pageSize*3, this.pageSize*5];
						}
					}
				});
			},
			sortClick(type){
				if(this.sortType==type){
					if(this.sortOrder == 'desc'){
						this.sortOrder = 'asc'
					}else{
						this.sortOrder = 'desc'
					}
				}else{
					this.sortType = type
					this.sortOrder = 'desc'
				}
				this.getList(1, '全部')
			},
			curChange(page) {
				this.getList(page);
			},
			prevClick(page) {
				this.getList(page);
			},
			sizeChange(size){
				this.pageSize = size
				this.getList(1);
			},
			nextClick(page) {
				this.getList(page);
			},
			imgPreView(url){
				this.previewImg = url
				this.previewVisible = true
			},
			toDetail(item) {
				let params = {
					id: item.id
				}
				if(this.centerType){
					params.centerType = 1
				}
				this.$router.push({path: '/index/shangpinxinxiDetail', query: params});
			},
			btnAuth(tableName,key){
				if(this.centerType){
					return this.isBackAuth(tableName,key)
				}else{
					return this.isAuth(tableName,key)
				}
			},
			backClick() {
				this.$router.push({path: '/index/center'});
			},
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.list-preview {
		padding: 30px calc((100% - 1200px)/2);
		background: #EDF0FA;
		display: flex;
		width: 100%;
		align-items: flex-start;
		position: relative;
		flex-wrap: wrap;
		.list-form-pv {
			padding: 10px;
			margin: 0  auto;
			background: none;
			display: flex;
			width: 1200px;
			align-items: center;
			flex-wrap: wrap;
			height: auto;
			order: 1;
			.list-item {
				margin: 0 10px 10px 0;
				background: none;
				width: auto;
				/deep/.el-form-item__content {
					display: flex;
				}
				.lable {
					padding: 0;
					color: #44446D;
					white-space: nowrap;
					display: inline-block;
					width: auto;
					font-size: 14px;
					line-height: 42px;
					text-align: center;
				}
				.el-input {
					width: calc(100% - 0px);
				}
				.datetimerange {
					border: 1px solid #44446D;
					border-radius: 30px;
					padding: 3px 10px;
					outline: none;
					background: #fff;
					width: 100%;
					justify-content: center;
				}
				.el-input /deep/ .el-input__inner {
					border: 1px solid #44446D;
					border-radius: 20px;
					padding: 0 10px;
					margin: 0;
					color: #333;
					width: 100%;
					font-size: 14px;
					line-height: 42px;
					height: 42px;
				}
				.el-select {
					width: 100%;
				}
				.el-select /deep/ .el-input__inner {
				}
				.el-date-editor {
					width: calc(100% - 0px);
				}
				.el-date-editor /deep/ .el-input__inner {
					border: 1px solid #44446D;
					border-radius: 30px;
					padding: 0 30px;
					margin: 0;
					outline: none;
					color: #333;
					width: 100%;
					font-size: 14px;
					line-height: 42px;
					height: 42px;
				}
			}
			.list-search-btn {
				cursor: pointer;
				border: 0;
				border-radius: 30px;
				padding: 0px 15px;
				margin: 0 10px 10px 0;
				outline: none;
				color: #fff;
				background: #FFD99D;
				width: auto;
				font-size: 14px;
				line-height: 42px;
				height: 42px;
				i {
					margin: 0 10px 0 0;
					color: #fff;
					font-size: 14px;
				}
			}
			.list-add-btn {
				cursor: pointer;
				border: 0;
				border-radius: 30px;
				padding: 0px 15px;
				margin: 0 10px 10px 0;
				outline: none;
				color: #FFFFFF;
				background: #44446D;
				width: auto;
				font-size: 14px;
				line-height: 42px;
				height: 42px;
				i {
					margin: 0 10px 0 0;
					color: inherit;
					font-size: inherit;
				}
			}
		}
		.select2 {
			margin: 0  auto;
			width: 1200px;
			height: auto;
			order: 2;
			.select2-list {
				border: 1px solid #44446D;
				border-radius: 0;
				margin: 10px 0;
				background: #CCDAF1;
				display: inline-block;
				width: 100%;
				position: relative;
				flex-wrap: wrap;
				height: auto;
				.label {
					padding: 0 5px;
					margin: 0 0 0 20px;
					color: #000000;
					white-space: nowrap;
					font-weight: 400;
					display: inline-block;
					width: auto;
					font-size: 14px;
					line-height: 60px;
				}
				.item-body {
					padding: 0 10px;
					display: inline-block;
					line-height: 60px;
					flex-wrap: wrap;
					height: 60px;
					.item {
						cursor: pointer;
						padding: 0 20px;
						color: #000;
						background: none;
						display: inline-block;
						font-size: 14px;
						line-height: 60px;
					}
					.item:hover {
						padding: 0 20px;
						color: #fff;
						background: #44446D;
						text-align: center;
					}
					.item.active {
						padding: 0 20px;
						color: #fff;
						background: #44446D;
						display: inline-block;
						text-align: center;
					}
				}
			}
		}
		.sort_view {
			padding: 5px 10px;
			margin: 10px auto 0 ;
			background: #CCDAF1;
			display: flex;
			width: 100%;
			border-color: #44446D;
			border-width: 0 0 2px 0;
			border-style: solid;
			flex-wrap: wrap;
			height: auto;
			order: 2;
			.price-sort-btn {
				border: 0;
				border-radius: 8px;
				padding: 0 15px;
				margin: 0 5px;
				background: none;
				.icon {
					margin: 0 2px 0 0;
					color: #626262;
					font-size: 14px;
					line-height: 40px;
				}
				.text {
					color: #626262;
					font-size: 14px;
					line-height: 40px;
				}
			}
			.click-sort-btn {
				border: 0;
				border-radius: 8px;
				padding: 0 15px;
				margin: 0 5px;
				background: none;
				.icon {
					margin: 0 2px 0 0;
					color: #626262;
					font-size: 14px;
					line-height: 40px;
				}
				.text {
					color: #626262;
					font-size: 14px;
					line-height: 40px;
				}
			}
			.collect-sort-btn {
				border: 0;
				border-radius: 8px;
				padding: 0 15px;
				margin: 0 5px;
				background: none;
				.icon {
					margin: 0 2px 0 0;
					color: #626262;
					font-size: 14px;
					line-height: 40px;
				}
				.text {
					color: #626262;
					font-size: 14px;
					line-height: 40px;
				}
			}
			.like-sort-btn {
				border: 0;
				border-radius: 8px;
				padding: 0 15px;
				margin: 0 5px;
				background: none;
				.icon {
					margin: 0 2px 0 0;
					color: #626262;
					font-size: 14px;
					line-height: 40px;
				}
				.text {
					color: #626262;
					font-size: 14px;
					line-height: 40px;
				}
			}
		}
		.list {
			margin: 0 auto;
			width: 1200px;
			order: 4;
			.index-pv1 .animation-box {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				z-index: initial;
			}
				
			.index-pv1 .animation-box:hover {
				transform: rotate(0) scale(1.01) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
			}
				
			.index-pv1 .animation-box img {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
			}
			
			.index-pv1 .animation-box img:hover {
				transform: rotate(0) scale(0.99) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
			.list3 {
				padding: 0;
				display: flex;
				width: 100%;
				flex-wrap: wrap;
				height: auto;
				.list-item {
					border: 1px solid #44446D;
					cursor: pointer;
					padding: 10px;
					margin: 10px;
					align-content: center;
					background: #CCDAF1;
					display: flex;
					width: calc(50% - 20px);
					align-items: center;
					position: relative;
					height: auto;
					.img {
						width: auto;
						.image {
							border: 1px solid #44446D;
							padding: 10px;
							object-fit: cover;
							display: block;
							width: 280px;
							height: 280px;
						}
					}
					.item-info {
						padding: 0 10px;
						overflow: hidden;
						flex: 1;
						display: flex;
						flex-wrap: wrap;
						height: auto;
						.name {
							padding: 0 10px;
							color: #000000;
							font-size: 14px;
							border-color: #44446D;
							border-width: 0 0 1px 0;
							line-height: 36px;
							border-style: solid;
						}
						.price {
							padding: 0 10px;
							color: #f00;
							font-size: 18px;
							border-color: #44446D;
							border-width: 0 0 1px 0;
							line-height: 36px;
							border-style: solid;
						}
						.time_item {
							padding: 0 10px;
							border-color: #44446D;
							border-width: 0 0 1px 0;
							border-style: solid;
							.icon {
								margin: 0 2px 0 0;
								color: #44446D;
								font-size: 12px;
								line-height: 28px;
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
							border-color: #44446D;
							border-width: 0 0 1px 0;
							border-style: solid;
							.icon {
								margin: 0 2px 0 0;
								color: #44446D;
								font-size: 12px;
								line-height: 28px;
							}
							.label {
								color: #44446D;
								font-size: 12px;
								line-height: 1.5;
							}
							.text {
								color: #44446D;
								font-size: 12px;
								line-height: 28px;
							}
						}
						.like_item {
							padding: 0 10px;
							border-color: #44446D;
							border-width: 0 0 1px 0;
							border-style: solid;
							.icon {
								margin: 0 2px 0 0;
								color: #44446D;
								font-size: 12px;
								line-height: 28px;
							}
							.label {
								color: #44446D;
								font-size: 12px;
								line-height: 1.5;
							}
							.text {
								color: #666;
								font-size: 12px;
								line-height: 28px;
							}
						}
						.collect_item {
							padding: 0 10px;
							border-color: #44446D;
							border-width: 0 0 1px 0;
							border-style: solid;
							.icon {
								margin: 0 2px 0 0;
								color: #44446D;
								font-size: 12px;
								line-height: 28px;
							}
							.label {
								color: #44446D;
								font-size: 12px;
								line-height: 1.5;
							}
							.text {
								color: #44446D;
								font-size: 12px;
								line-height: 28px;
							}
						}
						.view_item {
							padding: 0 10px;
							.icon {
								margin: 0 2px 0 0;
								color: #44446D;
								font-size: 12px;
								line-height: 28px;
							}
							.label {
								color: #44446D;
								font-size: 12px;
								line-height: 1.5;
							}
							.text {
								color: #44446D;
								font-size: 12px;
								line-height: 28px;
							}
						}
					}
					.desc {
						color: #44446D;
						flex: 1;
						display: none;
						font-size: 12px;
						line-height: 1.5;
					}
				}
				.list-item:hover {
					background: #44446D;
					.item-info {
						.name {
							color: #fff;
						}
						.price {
							color: #fff;
						}
						.time_item {
							.icon {
								color: #fff;
							}
							.label {
								color: #fff;
							}
							.text {
								color: #fff;
							}
						}
						.publisher_item {
							.icon {
								color: #fff;
							}
							.label {
								color: #fff;
							}
							.text {
								color: #fff;
							}
						}
						.like_item {
							.icon {
								color: #fff;
							}
							.label {
								color: #fff;
							}
							.text {
								color: #fff;
							}
						}
						.collect_item {
							.icon {
								color: #fff;
							}
							.label {
								color: #fff;
							}
							.text {
								color: #fff;
							}
						}
						.view_item {
							.icon {
								color: #fff;
							}
							.label {
								color: #fff;
							}
							.text {
								color: #fff;
							}
						}
					}
					.desc {
						color: #fff;
					}
				}
			}
		}
	}
</style>
