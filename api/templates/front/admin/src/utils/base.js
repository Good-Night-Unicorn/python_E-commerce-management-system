const base = {
    get() {
        return {
            url : "http://localhost:8080/python4nrl1242/",
            name: "python4nrl1242",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/front/dist/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "基于Flask和Vue的电商管理系统"
        } 
    }
}
export default base
