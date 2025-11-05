export default {
	baseUrl: 'http://localhost:8080/python4nrl1242/',
	name: '/python4nrl1242',
	indexNav: [
		{
			name: '广告信息',
			url: '/index/guanggaoxinxi',
		},
		{
			name: '商品信息',
			url: '/index/shangpinxinxi',
		},
		{
			name: '交流论坛',
			url: '/index/forum'
		}, 
		{
			name: '系统公告',
			url: '/index/news'
		},
	],
	cateList: [
		{
			name: '交流论坛',
			refTable: 'forumtype',
			refColumn: 'typename',
		},
		{
			name: '系统公告',
			refTable: 'newstype',
			refColumn: 'typename',
		},
	]
}
