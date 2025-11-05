<template>
	<div class="home-preview">




		<!-- 新闻资讯 -->
		<div id="animate_newsnews" class="news animate__animated">
			<div class="news_title_box">
				<span class="news_title">系统公告</span>
				<span class="news_subhead">{{'news'.toUpperCase()}}</span>
			</div>
			<div class="list list15 index-pv1">
				<div class="tab">
					<div class="item" :class="newsIndex15 == 0 ? 'active' : ''" @click="newsIndexClick15(0)">
						<div>全部</div>
					</div>
					<template v-for="(item,index) in newsCategoryList15">
						<div v-if="index < 6" class="item" :class="newsIndex15 == index + 1 ? 'active' : ''" @click="newsIndexClick15(index+1)">
							<div>{{item.typename}}</div>
						</div>
					</template>
					<div class="more" @click="moreBtn('news')">
						<div>更多</div>
						<span class="icon iconfont icon-jiantou25"></span>
					</div>
				</div>
				<div v-if="newsList.length" class="content">
					<div @click="toDetail('newsDetail', newsList[0])" class="left list-item animation-box">
						<img :src="baseUrl + newsList[0].picture">
						<div class="name">{{newsList[0].title}}</div>
						<div class="desc">{{newsList[0].introduction}}</div>
						<div class="time_item">
							<span class="icon iconfont icon-shijian21"></span>
							<span class="label">发布时间：</span>
							<span class="text">{{newsList[0].addtime.split(' ')[0]}}</span>
						</div>
						<div class="publisher_item">
							<span class="icon iconfont icon-geren16"></span>
							<span class="label">发布人：</span>
							<span class="text">{{newsList[0].name}}</span>
						</div>
						<div class="like_item">
							<span class="icon iconfont icon-zan10"></span>
							<span class="label">点赞数：</span>
							<span class="text">{{newsList[0].thumbsupnum}}</span>
						</div>
						<div class="collect_item">
							<span class="icon iconfont icon-shoucang10"></span>
							<span class="label">收藏量：</span>
							<span class="text">{{newsList[0].storeupnum}}</span>
						</div>
						<div class="view_item">
							<span class="icon iconfont icon-chakan9"></span>
							<span class="label">点击量：</span>
							<span class="text">{{newsList[0].clicknum}}</span>
						</div>
					</div>
					<div v-if="newsList.length > 1" class="right">
						<template v-for="(item,index) in newsList">
							<div v-if="index > 0" @click="toDetail('newsDetail', item)" class="list-item animation-box">
								<div class="date">
									<div class="day">{{item.addtime.split(" ")[0].split("-")[2]}}</div>
									<div class="year">{{item.addtime.split(" ")[0].split("-")[0] + '-' + item.addtime.split(" ")[0].split("-")[1]}}</div>
								</div>
								<div class="info">
									<div class="name">{{item.title}}</div>
									<div class="desc">{{item.introduction}}</div>
									<div class="publisher">
										<span class="icon iconfont icon-geren16"></span>
										<span class="label">发布人：</span>
										<span class="text">{{item.name}}</span>
									</div>
									<div class="like">
										<span class="icon iconfont icon-zan10"></span>
										<span class="label">点赞数：</span>
										<span class="text">{{item.thumbsupnum}}</span>
									</div>
									<div class="collect">
										<span class="icon iconfont icon-shoucang10"></span>
										<span class="label">收藏量：</span>
										<span class="text">{{item.storeupnum}}</span>
									</div>
									<div class="view">
										<span class="icon iconfont icon-chakan9"></span>
										<span class="label">点击量：</span>
										<span class="text">{{item.clicknum}}</span>
									</div>
								</div>
							</div>
						</template>
					</div>
				</div>
			</div>
			<div class="moreBtn" @click="moreBtn('news')">
				<span class="text">查看更多</span>
				<i class="icon iconfont icon-gengduo1"></i>
			</div>
		</div>
		<!-- 新闻资讯 -->
		<!-- 商品推荐 -->
		<div id="animate_recommendshangpinxinxi" class="recommend animate__animated">
			<div class="recommend_title_box">
				<span class="recommend_title">商品信息推荐</span>
				<span class="recommend_subhead">{{'shangpinxinxi'.toUpperCase()}} RECOMMEND</span>
			</div>
			<!-- 样式九 -->
			<div class="list list9 index-pv1">
				<div class="list-body-top">
					<div v-if="shangpinxinxiRecommend.length>0" @click="toDetail('shangpinxinxiDetail', shangpinxinxiRecommend[0])" class="list-item1 animation-box">
						<img v-if="preHttp(shangpinxinxiRecommend[0].tupian)&&preHttp2(shangpinxinxiRecommend[0].tupian)" :src="shangpinxinxiRecommend[0].tupian" alt="" />
						<img v-else-if="preHttp(shangpinxinxiRecommend[0].tupian)" :src="shangpinxinxiRecommend[0].tupian.split(',')[0]" alt="" />
						<img v-else :src="baseUrl + (shangpinxinxiRecommend[0].tupian?shangpinxinxiRecommend[0].tupian.split(',')[0]:'')" alt="" />
						<div class="infoBox">
							<div class="name">{{shangpinxinxiRecommend[0].shangpinmingcheng}}</div>
							<div class="price">￥{{shangpinxinxiRecommend[0].price}}</div>
							<div class="time_item">
								<span class="icon iconfont icon-shijian21"></span>
								<span class="label">发布时间：</span>
								<span class="text">{{shangpinxinxiRecommend[0].addtime.split(' ')[0]}}</span>
							</div>
							<div class="like_item">
								<span class="icon iconfont icon-zan10"></span>
								<span class="label">点赞数：</span>
								<span class="text">{{shangpinxinxiRecommend[0].thumbsupnum}}</span>
							</div>
							<div class="collect_item">
								<span class="icon iconfont icon-shoucang10"></span>
								<span class="label">收藏量：</span>
								<span class="text">{{shangpinxinxiRecommend[0].storeupnum}}</span>
							</div>
							<div class="view_item">
								<span class="icon iconfont icon-chakan9"></span>
								<span class="label">点击量：</span>
								<span class="text">{{shangpinxinxiRecommend[0].clicknum}}</span>
							</div>
						</div>
					</div>
					<div v-if="shangpinxinxiRecommend.length>1" @click="toDetail('shangpinxinxiDetail', shangpinxinxiRecommend[1])" class="list-item2 animation-box">
						<img v-if="preHttp(shangpinxinxiRecommend[1].tupian)&&preHttp2(shangpinxinxiRecommend[1].tupian)" :src="shangpinxinxiRecommend[1].tupian" alt="" />
						<img v-else-if="preHttp(shangpinxinxiRecommend[1].tupian)" :src="shangpinxinxiRecommend[1].tupian.split(',')[0]" alt="" />
						<img v-else :src="baseUrl + (shangpinxinxiRecommend[1].tupian?shangpinxinxiRecommend[1].tupian.split(',')[0]:'')" alt="" />
						<div class="infoBox">
							<div class="name">{{shangpinxinxiRecommend[1].shangpinmingcheng}}</div>
							<div class="price">￥{{shangpinxinxiRecommend[1].price}}</div>
							<div class="time_item">
								<span class="icon iconfont icon-shijian21"></span>
								<span class="label">发布时间：</span>
								<span class="text">{{shangpinxinxiRecommend[1].addtime.split(' ')[0]}}</span>
							</div>
							<div class="like_item">
								<span class="icon iconfont icon-zan10"></span>
								<span class="label">点赞数：</span>
								<span class="text">{{shangpinxinxiRecommend[1].thumbsupnum}}</span>
							</div>
							<div class="collect_item">
								<span class="icon iconfont icon-shoucang10"></span>
								<span class="label">收藏量：</span>
								<span class="text">{{shangpinxinxiRecommend[1].storeupnum}}</span>
							</div>
							<div class="view_item">
								<span class="icon iconfont icon-chakan9"></span>
								<span class="label">点击量：</span>
								<span class="text">{{shangpinxinxiRecommend[1].clicknum}}</span>
							</div>
						</div>
					</div>
				</div>
				<div class="list-body-bottom">
					<div v-if="shangpinxinxiRecommend.length>2" @click="toDetail('shangpinxinxiDetail', shangpinxinxiRecommend[2])" class="list-item1 animation-box">
						<img v-if="preHttp(shangpinxinxiRecommend[2].tupian)&&preHttp2(shangpinxinxiRecommend[2].tupian)" :src="shangpinxinxiRecommend[2].tupian" alt="" />
						<img v-else-if="preHttp(shangpinxinxiRecommend[2].tupian)" :src="shangpinxinxiRecommend[2].tupian.split(',')[0]" alt="" />
						<img v-else :src="baseUrl +  (shangpinxinxiRecommend[2].tupian?shangpinxinxiRecommend[2].tupian.split(',')[0]:'')" alt="" />
						<div class="infoBox">
							<div class="name">{{shangpinxinxiRecommend[2].shangpinmingcheng}}</div>
							<div class="price">￥{{shangpinxinxiRecommend[2].price}}</div>
							<div class="time_item">
								<span class="icon iconfont icon-shijian21"></span>
								<span class="label">发布时间：</span>
								<span class="text">{{shangpinxinxiRecommend[2].addtime.split(' ')[0]}}</span>
							</div>
							<div class="like_item">
								<span class="icon iconfont icon-zan10"></span>
								<span class="label">点赞数：</span>
								<span class="text">{{shangpinxinxiRecommend[2].thumbsupnum}}</span>
							</div>
							<div class="collect_item">
								<span class="icon iconfont icon-shoucang10"></span>
								<span class="label">收藏量：</span>
								<span class="text">{{shangpinxinxiRecommend[2].storeupnum}}</span>
							</div>
							<div class="view_item">
								<span class="icon iconfont icon-chakan9"></span>
								<span class="label">点击量：</span>
								<span class="text">{{shangpinxinxiRecommend[2].clicknum}}</span>
							</div>
						</div>
					</div>
					<div v-if="shangpinxinxiRecommend.length>3" @click="toDetail('shangpinxinxiDetail', shangpinxinxiRecommend[3])" class="list-item2 animation-box">
						<img v-if="preHttp(shangpinxinxiRecommend[3].tupian)&&preHttp2(shangpinxinxiRecommend[3].tupian)" :src="shangpinxinxiRecommend[3].tupian" alt="" />
						<img v-else-if="preHttp(shangpinxinxiRecommend[3].tupian)" :src="shangpinxinxiRecommend[3].tupian.split(',')[0]" alt="" />
						<img v-else :src="baseUrl + (shangpinxinxiRecommend[3].tupian?shangpinxinxiRecommend[3].tupian.split(',')[0]:'')" alt="" />
						<div class="infoBox">
							<div class="name">{{shangpinxinxiRecommend[3].shangpinmingcheng}}</div>
							<div class="price">￥{{shangpinxinxiRecommend[3].price}}</div>
							<div class="time_item">
								<span class="icon iconfont icon-shijian21"></span>
								<span class="label">发布时间：</span>
								<span class="text">{{shangpinxinxiRecommend[3].addtime.split(' ')[0]}}</span>
							</div>
							<div class="like_item">
								<span class="icon iconfont icon-zan10"></span>
								<span class="label">点赞数：</span>
								<span class="text">{{shangpinxinxiRecommend[3].thumbsupnum}}</span>
							</div>
							<div class="collect_item">
								<span class="icon iconfont icon-shoucang10"></span>
								<span class="label">收藏量：</span>
								<span class="text">{{shangpinxinxiRecommend[3].storeupnum}}</span>
							</div>
							<div class="view_item">
								<span class="icon iconfont icon-chakan9"></span>
								<span class="label">点击量：</span>
								<span class="text">{{shangpinxinxiRecommend[3].clicknum}}</span>
							</div>
						</div>
					</div>
					<div v-if="shangpinxinxiRecommend.length>4" @click="toDetail('shangpinxinxiDetail', shangpinxinxiRecommend[4])" class="list-item3 animation-box">
						<img v-if="preHttp(shangpinxinxiRecommend[4].tupian)&&preHttp2(shangpinxinxiRecommend[4].tupian)" :src="shangpinxinxiRecommend[4].tupian" alt="" />
						<img v-else-if="preHttp(shangpinxinxiRecommend[4].tupian)" :src="shangpinxinxiRecommend[4].tupian.split(',')[0]" alt="" />
						<img v-else :src="baseUrl + (shangpinxinxiRecommend[4].tupian?shangpinxinxiRecommend[4].tupian.split(',')[0]:'')" alt="" />
						<div class="infoBox">
							<div class="name">{{shangpinxinxiRecommend[4].shangpinmingcheng}}</div>
							<div class="price">￥{{shangpinxinxiRecommend[4].price}}</div>
							<div class="time_item">
								<span class="icon iconfont icon-shijian21"></span>
								<span class="label">发布时间：</span>
								<span class="text">{{shangpinxinxiRecommend[4].addtime.split(' ')[0]}}</span>
							</div>
							<div class="like_item">
								<span class="icon iconfont icon-zan10"></span>
								<span class="label">点赞数：</span>
								<span class="text">{{shangpinxinxiRecommend[4].thumbsupnum}}</span>
							</div>
							<div class="collect_item">
								<span class="icon iconfont icon-shoucang10"></span>
								<span class="label">收藏量：</span>
								<span class="text">{{shangpinxinxiRecommend[4].storeupnum}}</span>
							</div>
							<div class="view_item">
								<span class="icon iconfont icon-chakan9"></span>
								<span class="label">点击量：</span>
								<span class="text">{{shangpinxinxiRecommend[4].clicknum}}</span>
							</div>
						</div>
					</div>
				</div>
			</div>
			<div class="moreBtn" @click="moreBtn('shangpinxinxi')">
				<span class="text">查看更多</span>
				<i class="icon iconfont icon-gengduo1"></i>
			</div>
		</div>
		<!-- 商品推荐 -->
	</div>
</template>

<script>
import 'animate.css'
import Swiper from "swiper";

	export default {
		//数据集合
		data() {
			return {
				baseUrl: '',
				newsList: [],
				shangpinxinxiRecommend: [],


				newsIndex15: 0,
				newsCategoryList15: [],



			}
		},
		created() {
			this.baseUrl = this.$config.baseUrl;
			this.getNewsList();
			this.getNewsCategory()
			this.getList();
		},
		mounted() {
			window.addEventListener('scroll', this.handleScroll)
			setTimeout(()=>{
				this.handleScroll()
			},100)
			
			this.swiperChanges()
		},
		beforeDestroy() {
			window.removeEventListener('scroll', this.handleScroll)
		},
		//方法集合
		methods: {
			swiperChanges() {
				setTimeout(()=>{
				},750)
			},
			newsIndexClick15(index) {
				this.newsIndex15 = index
				this.getNewsList()
			},
			getNewsCategory() {
				this.$http.get('newstype/list', {}).then(res => {
					if (res.data.code == 0) {
						this.newsCategoryList15 = res.data.data
					}
				});
			},

			listIndexClick12(index, name) {
				this['listIndex12' + name] = index
				this.getList()
				
				document.querySelectorAll('.lists .list12' + name + ' .list .item').forEach(el => {
				  el.classList.remove("active")
				})
				setTimeout(() => {
				  document.querySelectorAll('.lists .list12' + name + ' .list .item').forEach(el => {
					el.classList.add("active")
				  })
				}, 1);
			},

			handleScroll() {
				let arr = [
					{id:'about',css:'animate__'},
					{id:'system',css:'animate__'},
					{id:'animate_recommendshangpinxinxi',css:'animate__'},
					{id:'animate_newsnews',css:'animate__'},
				]
			
				for (let i in arr) {
					let doc = document.getElementById(arr[i].id)
					if (doc) {
						let top = doc.offsetTop
						let win_top = window.innerHeight + window.pageYOffset
						// console.log(top,win_top)
						if (win_top > top && doc.classList.value.indexOf(arr[i].css) < 0) {
							// console.log(doc)
							doc.classList.add(arr[i].css)
						}
					}
				}
			},
			preHttp(str) {
				return str && str.substr(0,4)=='http';
			},
			preHttp2(str) {
				return str && str.split(',w').length>1;
			},
			getNewsList() {
				let data = {
					page: 1,
					limit: 7,
					sort: 'addtime',
					order: 'desc'
				}
				if(this.newsIndex15!=0) {
					data['typename'] = this.newsCategoryList15[this.newsIndex15 - 1].typename
				}
				this.$http.get('news/list', {params: data}).then(res => {
					if (res.data.code == 0) {
						this.newsList = res.data.data.list;
					
					}
				});
			},
			getList() {
				let autoSortUrl = "";
				let data = {}
				autoSortUrl = "shangpinxinxi/autoSort";
				if(localStorage.getItem('frontToken')) {
					autoSortUrl = "shangpinxinxi/autoSort2";
				}
				data = {
					page: 1,
					limit: 5,
					onshelves: 1,
				}
				this.$http.get(autoSortUrl, {params: data}).then(res => {
					if (res.data.code == 0) {
						this.shangpinxinxiRecommend = res.data.data.list;
					}
				});
			
			},
			toDetail(path, item) {
				this.$router.push({path: '/index/' + path, query: {id: item.id}});
			},
			moreBtn(path) {
				this.$router.push({path: '/index/' + path});
			}
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.home-preview {
		padding: 0;
		overflow: hidden;
		flex-direction: column;
		background: #EDF0FA;
		display: flex;
		width: 100%;
		.news {
			padding: 40px 0;
			margin: 0;
			background: #C0DDE3;
			width: 100%;
			position: relative;
			order: 5;
			.news_title_box {
				padding: 0  165px;
				margin: 0px auto 20px ;
				flex-direction: column;
				background: url(http://codegen.caihongy.cn/20250118/8fc0638edcbd47b4bdaa28e8495ba36b.png) no-repeat center center / 100% 100%;
				display: flex;
				width: 1200px;
				line-height: 100px;
				justify-content: flex-end;
				align-items: center;
				text-align: left;
				height: 100px;
				.news_title {
					padding: 0 0 0 35px;
					color: #44446D;
					background: none;
					font-weight: 500;
					width: 100%;
					font-size: 32px;
					text-align: left;
					order: 1;
				}
				.news_subhead {
					padding: 0 0 0 35px;
					max-height: 3em;
					margin: 0;
					overflow: hidden;
					color: #3F3F3F;
					font-weight: bold;
					display: -webkit-box;
					width: 100%;
					font-size: 24px;
					line-height: 1.5;
					text-overflow: ellipsis;
					text-align: left;
				}
			}
			.index-pv1 .animation-box:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
			}
			.index-pv1 .animation-box img:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
			.list15 {
				border: 5px solid #44446D;
				border-radius: 0 90px 0 0 ;
				box-shadow: 10px 10px 0px 0px rgb(68, 68, 109);
				margin: 0 auto;
				overflow: hidden;
				background: #EDF0FA;
				width: 1200px;
				height: auto;
				.tab {
					border-radius: 0px 0px 20px 20px;
					padding: 0 0 0 10px;
					margin: 0 0 20px;
					background: #FFD99D;
					display: flex;
					width: 100%;
					position: relative;
					height: 99px;
					.item {
						cursor: pointer;
						border: 0;
						padding: 0 20px;
						margin: auto 10px;
						color: #333;
						background: #EDF0FA;
						display: flex;
						width: auto;
						font-size: 16px;
						line-height: 50px;
						align-items: center;
						height: 50px;
					}
					
					.item:hover {
						color: #fff;
						background: #44446D;
					}
					
					.item.active {
						color: #fff;
						background: #44446D;
					}
					.more {
						cursor: pointer;
						padding: 5px 10px;
						margin: 0 10px;
						color: #fff;
						background: #44446D;
						display: none;
						width: 180px;
						line-height: 44px;
						position: absolute;
						right: 0%;
						text-align: center;
					}
					
					.more:hover {
						cursor: pointer;
						padding: 5px 10px;
						margin: 0 10px;
						color: #fff;
						background: #44446D;
						display: flex;
						width: 180px;
						line-height: 44px;
						position: absolute;
						right: 0%;
						text-align: center;
					}
				}
				.content {
					padding: 0 20px 54px 20px;
					display: flex;
					width: 100%;
					justify-content: space-between;
					height: auto;
					.left.list-item {
						border: 1px solid #44446D;
						padding: 20px;
						margin: 10px 0 0;
						background: #EDF0FA;
						display: flex;
						width: 380px;
						flex-wrap: wrap;
						height: auto;
						img {
							margin: 0 0 20px 0;
							object-fit: cover;
							display: block;
							width: 100%;
							height: 200px;
						}
						.name {
							padding: 0 10px;
							overflow: hidden;
							color: #000000;
							white-space: nowrap;
							width: 100%;
							font-size: 16px;
							line-height: 1.5;
							text-overflow: ellipsis;
						}
						.desc {
							padding: 0 10px;
							margin: 0 0 5px 0;
							overflow: hidden;
							color: #555555;
							width: 100%;
							font-size: 14px;
							line-height: 24px;
							height: 48px;
						}
						.time_item {
							padding: 0 10px;
							.icon {
								margin: 0 2px 0 0;
								color: #666;
								font-size: 12px;
								line-height: 1.5;
							}
							.label {
								color: #666;
								display: none;
								font-size: 12px;
								line-height: 1.5;
							}
							.text {
								color: #666;
								font-size: 12px;
								line-height: 1.5;
							}
						}
						.publisher_item {
							padding: 0 10px;
							.icon {
								margin: 0 2px 0 0;
								color: #666;
								font-size: 12px;
								line-height: 1.5;
							}
							.label {
								color: #666;
								display: none;
								font-size: 12px;
								line-height: 1.5;
							}
							.text {
								color: #666;
								font-size: 12px;
								line-height: 1.5;
							}
						}
						.like_item {
							padding: 0 10px;
							.icon {
								margin: 0 2px 0 0;
								color: #666;
								font-size: 12px;
								line-height: 1.5;
							}
							.label {
								color: #666;
								display: none;
								font-size: 12px;
								line-height: 1.5;
							}
							.text {
								color: #666;
								font-size: 12px;
								line-height: 1.5;
							}
						}
						.collect_item {
							padding: 0 10px;
							.icon {
								margin: 0 2px 0 0;
								color: #666;
								font-size: 12px;
								line-height: 1.5;
							}
							.label {
								color: #666;
								display: none;
								font-size: 12px;
								line-height: 1.5;
							}
							.text {
								color: #666;
								font-size: 12px;
								line-height: 1.5;
							}
						}
						.view_item {
							padding: 0 10px;
							.icon {
								margin: 0 2px 0 0;
								color: #666;
								font-size: 12px;
								line-height: 1.5;
							}
							.label {
								color: #666;
								display: none;
								font-size: 12px;
								line-height: 1.5;
							}
							.text {
								color: #666;
								font-size: 12px;
								line-height: 1.5;
							}
						}
					}
					.right {
						margin: 0 0 0 10px;
						display: flex;
						width: 770px;
						justify-content: space-between;
						flex-wrap: wrap;
						height: auto;
						.list-item  {
							border: 1px solid rgb(68, 68, 109);
							padding: 0;
							margin: 10px 0 0 0;
							background: none;
							display: flex;
							width: 380px;
							justify-content: space-between;
							height: auto;
							.date  {
								flex-direction: column;
								display: flex;
								width: 90px;
								border-color: #44446D;
								border-width: 0 1px 0  0 ;
								justify-content: center;
								align-items: center;
								border-style: solid;
								height: auto;
								.day  {
									color: #44446D;
									font-weight: 600;
									width: auto;
									font-size: 24px;
									line-height: 40px;
								}
								.year  {
									color: #999999;
									width: auto;
									font-size: 14px;
									line-height: 40px;
								}
							}
							.info {
								padding: 10px 0;
								flex: 1;
								.name  {
									padding: 0 10px;
									color: #000000;
									font-size: 14px;
									line-height: 1.5;
								}
								.desc  {
									padding: 0 10px;
									overflow: hidden;
									color: #555555;
									font-size: 14px;
									line-height: 24px;
									height: 48px;
								}
								.publisher {
									padding: 0 10px;
									display: inline-block;
									.icon {
										margin: 0 2px 0 0;
										color: #2222AA;
										font-size: 12px;
										line-height: 1.5;
									}
									.label {
										color: #666;
										display: none;
										font-size: 12px;
										line-height: 1.5;
									}
									.text {
										color: #2222AA;
										font-size: 12px;
										line-height: 1.5;
									}
								}
								.like {
									padding: 0 10px;
									display: inline-block;
									.icon {
										margin: 0 2px 0 0;
										color: #2222AA;
										font-size: 12px;
										line-height: 1.5;
									}
									.label {
										color: #666;
										display: none;
										font-size: 12px;
										line-height: 1.5;
									}
									.text {
										color: #2222AA;
										font-size: 12px;
										line-height: 1.5;
									}
								}
								.collect {
									padding: 0 10px;
									display: inline-block;
									.icon {
										margin: 0 2px 0 0;
										color: #2222AA;
										font-size: 12px;
										line-height: 1.5;
									}
									.label {
										color: #666;
										display: none;
										font-size: 12px;
										line-height: 1.5;
									}
									.text {
										color: #2222AA;
										font-size: 12px;
										line-height: 1.5;
									}
								}
								.view {
									padding: 0 10px;
									display: inline-block;
									.icon {
										margin: 0 2px 0 0;
										color: #2222AA;
										font-size: 12px;
										line-height: 1.5;
									}
									.label {
										color: #666;
										display: none;
										font-size: 12px;
										line-height: 1.5;
									}
									.text {
										color: #2222AA;
										font-size: 12px;
										line-height: 1.5;
									}
								}
							}
						}
						.list-item:hover  {
							background: rgba(255, 217, 157,0.5);
							.date {
								border-color: #fff;
								.day {
									color: #fff;
									border-color: #fff;
								}
								.year {
									color: #fff;
								}
							}
							.info {
								.name  {
									color: #fff;
								}
								.desc  {
									color: #fff;
								}
								.publisher {
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
								.like {
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
								.collect {
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
								.view {
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
						}
					}
				}
			}
			.moreBtn {
				border: 0;
				border-radius: 0 0 10px 10px;
				margin: 0;
				top: calc(7% - 12px);
				background: #44446D;
				display: block;
				width: 180px;
				line-height: 50px;
				position: absolute;
				right: 19%;
				text-align: center;
				.text {
					color: #fff;
					font-size: 15px;
				}
				.icon {
					color: #fff;
					font-size: 15px;
				}
			}
		}
		.recommend {
			padding: 40px 0;
			margin: 0;
			background: #C0DDE3;
			width: 100%;
			position: relative;
			order: 3;
			.recommend_title_box {
				padding: 0  165px;
				margin: 0px auto 20px ;
				flex-direction: column;
				background: url(http://codegen.caihongy.cn/20250118/8fc0638edcbd47b4bdaa28e8495ba36b.png) no-repeat center center / 100% 100%;
				display: flex;
				width: 1200px;
				line-height: 100px;
				justify-content: flex-end;
				align-items: center;
				text-align: left;
				height: 100px;
				.recommend_title {
					padding: 0 0 0 35px;
					color: #44446D;
					background: none;
					font-weight: 500;
					width: 100%;
					font-size: 32px;
					text-align: left;
					order: 1;
				}
				.recommend_subhead {
					color: #44446D;
					display: none;
					width: 100%;
				}
			}
			.index-pv1 .animation-box {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				z-index: initial;
			}
			
			.index-pv1 .animation-box:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 10px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
			}
			
			.index-pv1 .animation-box img {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
			}
			
			.index-pv1 .animation-box img:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
			.list9 {
				border: 5px solid rgb(63, 65, 107);
				border-radius: 0px 90px 0px 0px;
				padding: 40px 10px 60px 10px;
				box-shadow: 10px 10px 0px 0px rgb(68, 68, 109);
				margin: 0 auto;
				background: #EDF0FA;
				width: 1200px;
				height: auto;
				.list-body-top {
					margin: 0 0 20px;
					display: flex;
					width: 1180px;
					height: auto;
					.list-item1 {
						border: 2px solid rgb(68, 68, 109);
						padding: 30px;
						margin: 0 10px;
						display: inline-block;
						width: 570px;
						position: relative;
						height: 317px;
						img {
							object-fit: cover;
							width: 100%;
							float: left;
							height: 100%;
						}
						.infoBox {
							padding: 0 16px;
							align-content: center;
							left: 5%;
							bottom: 9%;
							background: #44446D80;
							display: flex;
							width: calc(100% - 60px);
							min-height: 50%;
							align-items: center;
							position: absolute;
							flex-wrap: wrap;
							.name {
								padding: 0;
								margin: 0px 0 0 0;
								overflow: hidden;
								color: #fff;
								white-space: nowrap;
								width: 100%;
								font-size: 16px;
								line-height: 24px;
								text-overflow: ellipsis;
							}
							.price {
								padding: 3px 0;
								color: #FF0000;
								width: 100%;
								font-size: 18px;
								line-height: 1.5;
							}
							.time_item {
								padding: 0 10px 0 0;
								.icon {
									margin: 0 2px 0 0;
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
								.label {
									color: #FFFFFF;
									display: none;
									font-size: 12px;
									line-height: 1.5;
								}
								.text {
									color: #FFFFFF;
									font-size: 12px;
									line-height: 1.5;
								}
							}
							.publisher_item {
								padding: 0 10px 0 0;
								.icon {
									margin: 0 2px 0 0;
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
								.label {
									color: #FFFFFF;
									display: none;
									font-size: 12px;
									line-height: 1.5;
								}
								.text {
									color: #FFFFFF;
									font-size: 12px;
									line-height: 1.5;
								}
							}
							.like_item {
								padding: 0 10px 0 0;
								.icon {
									margin: 0 2px 0 0;
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
								.label {
									color: #FFFFFF;
									display: none;
									font-size: 12px;
									line-height: 1.5;
								}
								.text {
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
							}
							.collect_item {
								padding: 0 10px 0 0;
								.icon {
									margin: 0 2px 0 0;
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
								.label {
									color: #FFFFFF;
									display: none;
									font-size: 12px;
									line-height: 1.5;
								}
								.text {
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
							}
							.view_item {
								padding: 0 10px 0 0;
								.icon {
									margin: 0 2px 0 0;
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
								.label {
									color: #FFFFFF;
									display: none;
									font-size: 12px;
									line-height: 1.5;
								}
								.text {
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
							}
						}
					}
					.list-item2 {
						border: 2px solid rgb(68, 68, 109);
						padding: 30px;
						margin: 0 10px;
						display: inline-block;
						width: 570px;
						position: relative;
						height: 317px;
						img {
							object-fit: cover;
							width: 100%;
							float: left;
							height: 100%;
						}
						.infoBox {
							padding: 0 16px;
							align-content: center;
							left: 5%;
							bottom: 9%;
							background: #44446D80;
							display: flex;
							width: calc(100% - 60px);
							min-height: 50%;
							align-items: center;
							position: absolute;
							flex-wrap: wrap;
							.name {
								padding: 0;
								margin: 0px 0 0 0;
								overflow: hidden;
								color: #fff;
								white-space: nowrap;
								width: 100%;
								font-size: 16px;
								line-height: 24px;
								text-overflow: ellipsis;
							}
							.price {
								padding: 0;
								color: #FF0000;
								width: 100%;
								font-size: 18px;
								line-height: 1.5;
							}
							.time_item {
								padding: 0 10px 0 0;
								.icon {
									margin: 0 2px 0 0;
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
								.label {
									color: #FFFFFF;
									display: none;
									font-size: 12px;
									line-height: 1.5;
								}
								.text {
									color: #FFFFFF;
									font-size: 12px;
									line-height: 1.5;
								}
							}
							.publisher_item {
								padding: 0 10px 0 0;
								.icon {
									margin: 0 2px 0 0;
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
								.label {
									color: #FFFFFF;
									display: none;
									font-size: 12px;
									line-height: 1.5;
								}
								.text {
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
							}
							.like_item {
								padding: 0 10px 0 0;
								.icon {
									margin: 0 2px 0 0;
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
								.label {
									color: #FFFFFF;
									display: none;
									font-size: 12px;
									line-height: 1.5;
								}
								.text {
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
							}
							.collect_item {
								padding: 0 10px 0 0;
								.icon {
									margin: 0 2px 0 0;
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
								.label {
									color: #FFFFFF;
									display: none;
									font-size: 12px;
									line-height: 1.5;
								}
								.text {
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
							}
							.view_item {
								padding: 0 10px 0 0;
								.icon {
									margin: 0 2px 0 0;
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
								.label {
									color: #FFFFFF;
									display: none;
									font-size: 12px;
									line-height: 1.5;
								}
								.text {
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
							}
						}
					}
				}
				.list-body-bottom {
					display: flex;
					width: 1180px;
					justify-content: space-between;
					height: 400px;
					.list-item1 {
						border: 2px solid rgb(68, 68, 109);
						padding: 30px;
						margin: 0 10px;
						display: inline-block;
						width: 390px;
						position: relative;
						height: 400px;
						img {
							object-fit: cover;
							width: 100%;
							float: left;
							height: 100%;
						}
						.infoBox {
							padding: 0 16px;
							align-content: center;
							bottom: calc(8% - 2px);
							background: #44446D80;
							display: flex;
							width: calc(100% - 60px);
							align-items: center;
							position: absolute;
							flex-wrap: wrap;
							height: 50%;
							.name {
								padding: 0;
								margin: 0px 0 0 0;
								overflow: hidden;
								color: #fff;
								white-space: nowrap;
								width: 100%;
								font-size: 16px;
								line-height: 24px;
								text-overflow: ellipsis;
							}
							.price {
								padding: 0;
								color: #FF0000;
								width: 100%;
								font-size: 18px;
								line-height: 1.5;
							}
							.time_item {
								padding: 0 10px 0 0;
								.icon {
									margin: 0 2px 0 0;
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
								.label {
									color: #FFFFFF;
									display: none;
									font-size: 12px;
									line-height: 1.5;
								}
								.text {
									color: #FFFFFF;
									font-size: 12px;
									line-height: 1.5;
								}
							}
							.publisher_item {
								padding: 0 10px 0 0;
								.icon {
									margin: 0 2px 0 0;
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
								.label {
									color: #FFFFFF;
									display: none;
									font-size: 12px;
									line-height: 1.5;
								}
								.text {
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
							}
							.like_item {
								padding: 0 10px 0 0;
								.icon {
									margin: 0 2px 0 0;
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
								.label {
									color: #FFFFFF;
									display: none;
									font-size: 12px;
									line-height: 1.5;
								}
								.text {
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
							}
							.collect_item {
								padding: 0 10px 0 0;
								.icon {
									margin: 0 2px 0 0;
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
								.label {
									color: #FFFFFF;
									display: none;
									font-size: 12px;
									line-height: 1.5;
								}
								.text {
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
							}
							.view_item {
								padding: 0 10px 0 0;
								.icon {
									margin: 0 2px 0 0;
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
								.label {
									color: #FFFFFF;
									display: none;
									font-size: 12px;
									line-height: 1.5;
								}
								.text {
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
							}
						}
					}
					.list-item2 {
						border: 2px solid rgb(68, 68, 109);
						padding: 30px;
						margin: 0 10px;
						display: inline-block;
						width: 390px;
						position: relative;
						height: 400px;
						img {
							object-fit: cover;
							width: 100%;
							float: left;
							height: 100%;
						}
						.infoBox {
							padding: 0 16px;
							align-content: center;
							bottom: calc(8% - 2px);
							background: #44446D80;
							display: flex;
							width: calc(100% - 60px);
							align-items: center;
							position: absolute;
							flex-wrap: wrap;
							height: 50%;
							.name {
								padding: 0;
								margin: 0px 0 0 0;
								overflow: hidden;
								color: #fff;
								white-space: nowrap;
								width: 100%;
								font-size: 16px;
								line-height: 24px;
								text-overflow: ellipsis;
							}
							.price {
								padding: 0;
								color: #FF0000;
								width: 100%;
								font-size: 18px;
								line-height: 1.5;
							}
							.time_item {
								padding: 0 10px 0 0;
								.icon {
									margin: 0 2px 0 0;
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
								.label {
									color: #666;
									display: none;
									font-size: 12px;
									line-height: 1.5;
								}
								.text {
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
							}
							.publisher_item {
								padding: 0 10px 0 0;
								.icon {
									margin: 0 2px 0 0;
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
								.label {
									color: #666;
									display: none;
									font-size: 12px;
									line-height: 1.5;
								}
								.text {
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
							}
							.like_item {
								padding: 0 10px 0 0;
								.icon {
									margin: 0 2px 0 0;
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
								.label {
									color: #666;
									display: none;
									font-size: 12px;
									line-height: 1.5;
								}
								.text {
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
							}
							.collect_item {
								padding: 0 10px 0 0;
								.icon {
									margin: 0 2px 0 0;
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
								.label {
									color: #666;
									display: none;
									font-size: 12px;
									line-height: 1.5;
								}
								.text {
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
							}
							.view_item {
								padding: 0 10px 0 0;
								.icon {
									margin: 0 2px 0 0;
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
								.label {
									color: #fff;
									display: none;
									font-size: 12px;
									line-height: 1.5;
								}
								.text {
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
							}
						}
					}
					.list-item3 {
						border: 2px solid rgb(68, 68, 109);
						padding: 30px;
						margin: 0 10px;
						display: inline-block;
						width: 390px;
						position: relative;
						height: 400px;
						img {
							object-fit: cover;
							width: 100%;
							float: left;
							height: 100%;
						}
						.infoBox {
							padding: 0 16px;
							align-content: center;
							bottom: calc(8% - 2px);
							background: #44446D80;
							display: flex;
							width: calc(100% - 60px);
							align-items: center;
							position: absolute;
							flex-wrap: wrap;
							height: 50%;
							.name {
								padding: 0;
								margin: 0px 0 0 0;
								overflow: hidden;
								color: #fff;
								white-space: nowrap;
								width: 100%;
								font-size: 16px;
								line-height: 24px;
								text-overflow: ellipsis;
							}
							.price {
								padding: 0;
								color: #FF0000;
								width: 100%;
								font-size: 18px;
								line-height: 1.5;
							}
							.time_item {
								padding: 0 10px 0 0;
								.icon {
									margin: 0 2px 0 0;
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
								.label {
									color: #666;
									display: none;
									font-size: 12px;
									line-height: 1.5;
								}
								.text {
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
							}
							.publisher_item {
								padding: 0 10px 0 0;
								.icon {
									margin: 0 2px 0 0;
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
								.label {
									margin: 0 2px 0 0;
									color: #fff;
									display: none;
									font-size: 12px;
									line-height: 1.5;
								}
								.text {
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
							}
							.like_item {
								padding: 0 10px 0 0;
								.icon {
									margin: 0 2px 0 0;
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
								.label {
									margin: 0 2px 0 0;
									color: #fff;
									display: none;
									font-size: 12px;
									line-height: 1.5;
								}
								.text {
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
							}
							.collect_item {
								padding: 0 10px 0 0;
								.icon {
									margin: 0 2px 0 0;
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
								.label {
									margin: 0 2px 0 0;
									color: #fff;
									display: none;
									font-size: 12px;
									line-height: 1.5;
								}
								.text {
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
							}
							.view_item {
								padding: 0 10px 0 0;
								.icon {
									margin: 0 2px 0 0;
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
								.label {
									margin: 0 2px 0 0;
									color: #fff;
									display: none;
									font-size: 12px;
									line-height: 1.5;
								}
								.text {
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
							}
						}
					}
				}
			}
			.moreBtn {
				border: 0;
				border-radius: 0 0 10px 10px;
				margin: 0;
				top: calc(5% - 12px);
				background: #44446D;
				display: block;
				width: 180px;
				line-height: 50px;
				position: absolute;
				right: 19%;
				text-align: center;
				.text {
					color: #fff;
					font-size: 15px;
				}
				.icon {
					color: #fff;
					font-size: 15px;
				}
			}
		}
	}
</style>
