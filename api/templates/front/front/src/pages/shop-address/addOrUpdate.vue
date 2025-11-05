<template>
	<div :style='{"width":"100%","padding":"30px calc((100% - 1200px)/2)","margin":"0px auto","position":"relative","background":"#EDF0FA"}'>
		<el-form class="add-update-preview" ref="form" :model="form" :rules="rules" label-width="180px">
			<el-form-item :style='{"width":"100%","padding":"10px","margin":"0 0 10px","background":"none","display":"inline-block"}' label="联系人" prop="name">
				<el-input v-model="form.name" placeholder="联系人"></el-input>
			</el-form-item>
			<el-form-item :style='{"width":"100%","padding":"10px","margin":"0 0 10px","background":"none","display":"inline-block"}' label="手机号码" prop="phone">
				<el-input v-model="form.phone" placeholder="手机号码"></el-input>
			</el-form-item>
			<el-form-item :style='{"width":"100%","padding":"10px","margin":"0 0 10px","background":"none","display":"inline-block"}' label="默认地址">
				<el-radio-group v-model="form.isdefault">
					<el-radio label="是"></el-radio>
					<el-radio label="否"></el-radio>
				</el-radio-group>
			</el-form-item>
			<el-form-item :style='{"width":"100%","padding":"10px","margin":"0 0 10px","background":"none","display":"inline-block"}' label="地址" prop="address">
				<el-input v-model="form.address" placeholder="请输入地址"></el-input>
			</el-form-item>
			<el-form-item :style='{"padding":"0","margin":"0","textAlign":"center","justifyContent":"center","display":"flex"}'>
				<el-button class="submitBtn" type="primary" @click="onSubmit('form')">
					<span class="icon iconfont icon-kaitongfuwu"></span>
					<span class="text">添加</span>
				</el-button>
				<el-button v-if="!isBuy" class="closeBtn" @click="goBack">
					<span class="icon iconfont icon-shanchu1"></span>
					<span class="text">取消</span>
				</el-button>
			</el-form-item>
		</el-form>
	</div>
</template>

<script>
	import { Loading } from 'element-ui';
	export default {
		//数据集合
		data() {
			return {
				form: {
					userid: Number(localStorage.getItem('frontUserid')),
					name: localStorage.getItem('username'),
					phone: '',
					isdefault: '是',
					address: ''
				},
				rules: {
					name: [{ required: true, message: '请输入联系人', trigger: 'blur' }],
					phone: [
						{ required: true, message: '请输入手机号码', trigger: 'blur' },
						{ required: true, validator: this.$validate.isMobile, trigger: 'blur' }
					],
					address: [{ required: true, message: '请选择收货地址', trigger: 'blur' }]
				},
				isEdit: false,
				isBuy: false
			}
		},
		created() {
			if (this.$route.query.id != undefined) {
				this.isEdit = true;
				this.form = Object.assign({}, JSON.parse(this.$route.query.editObj));
			}
		},
		//方法集合
		methods: {
			buyAdd(){
				this.isBuy = true
			},
			onSubmit(formName) {
				this.$refs[formName].validate((valid) => {
					if (valid) {
						this.$http.post(`address/${this.isEdit ? 'update' : 'add'}`, this.form).then(res => {
							if (res.data.code == 0) {
								this.$message({
									message: `${this.isEdit ? '更新' : '添加'}成功`,
									type: 'success',
									duration: 1500,
									onClose: () => {
										if(this.isBuy){
											this.$emit('change')
										}else{
											this.$router.go(-1);
									  }
									}
								});
							}
						});
					} else {
						return false;
					}
				});
			},
			getAddr() {
				if (this.address == '') {
					this.$message({
						message: '地址不能为空',
						type: 'error',
						duration: 1500
					});
					return;
				}
				this.form.address = this.address;
				this.dialogVisible = false;
			},
			goBack() {
				this.$router.go(-1);
			},
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.add-update-preview .el-form-item /deep/ .el-form-item__label {
		padding: 0 10px 0 0;
		margin: 0;
		color: #2C3657;
		font-weight: 500;
		width: 180px;
		font-size: 16px;
		line-height: 50px;
		text-align: right;
	}
	
	.add-update-preview .el-form-item /deep/ .el-form-item__content {
		margin-left: 180px;
	}
	
	.add-update-preview .el-input /deep/ .el-input__inner {
		border: 0px solid #BBB09B;
		border-radius: 10px;
		padding: 0 12px;
		box-shadow: 0 0 0px rgba(64, 158, 255, .5);
		outline: none;
		color: #000;
		background: #FFFFFF;
		width: 100%;
		font-size: 15px;
		line-height: 50px;
		height: 50px;
	}
	
	.add-update-preview .el-select /deep/ .el-input__inner {
		border: 0px solid #BBB09B;
		border-radius: 10px;
		padding: 0 10px;
		box-shadow: 0 0 0px rgba(64, 158, 255, .5);
		outline: none;
		color: #000;
		width: 100%;
		font-size: 15px;
		height: 50px;
	}
	
	.add-update-preview .el-date-editor /deep/ .el-input__inner {
		border: 0px solid #BBB09B;
		border-radius: 10px;
		padding: 0 10px 0 30px;
		box-shadow: 0 0 0px rgba(64, 158, 255, .5);
		outline: none;
		color: #000;
		width: 100%;
		font-size: 15px;
		height: 50px;
	}
	
	.add-update-preview /deep/ .el-upload--picture-card {
		background: transparent;
		border: 0;
		border-radius: 0;
		width: auto;
		height: auto;
		line-height: initial;
		vertical-align: middle;
	}
	
	.add-update-preview /deep/ .upload .upload-img {
		border: 0px solid #BBB09B;
		cursor: pointer;
		border-radius: 6px;
		color: #000;
		background: #FFFFFF;
		width: 150px;
		font-size: 32px;
		line-height: 60px;
		text-align: center;
		height: 60px;
	}
	
	.add-update-preview /deep/ .el-upload-list .el-upload-list__item {
		border: 0px solid #BBB09B;
		cursor: pointer;
		border-radius: 6px;
		color: #000;
		background: #FFFFFF;
		width: 150px;
		font-size: 32px;
		line-height: 60px;
		text-align: center;
		height: 60px;
	}
	
	.add-update-preview /deep/ .el-upload .el-icon-plus {
		border: 0px solid #BBB09B;
		cursor: pointer;
		border-radius: 6px;
		color: #000;
		background: #FFFFFF;
		width: 150px;
		font-size: 32px;
		line-height: 60px;
		text-align: center;
		height: 60px;
	}
	
	.add-update-preview .el-textarea /deep/ .el-textarea__inner {
		border: 0px solid #BBB09B;
		border-radius: 10px;
		padding: 12px;
		box-shadow: 0 0 0px rgba(64, 158, 255, .5);
		outline: none;
		color: #000;
		width: 100%;
		font-size: 14px;
		height: 120px;
	}
    .map{
        height: 50vh;
    }
	.add-update-preview .submitBtn {
		border: 0;
		cursor: pointer;
		border-radius: 20px;
		padding: 0 35px;
		margin: 0 20px 0 0;
		outline: none;
		background: #44446D;
		display: inline-block;
		width: 150px;
		font-size: 14px;
		line-height: 50px;
		height: 50px;
		.icon {
			color: rgba(255, 255, 255, 1);
			display: none;
		}
		.text {
			color: rgba(255, 255, 255, 1);
		}
	}
	.add-update-preview .submitBtn:hover {
		opacity: 0.5;
		.icon {
			color: #000;
		}
		.text {
			color: #fff;
		}
	}
	.add-update-preview .closeBtn {
		border: 0;
		cursor: pointer;
		border-radius: 20px;
		padding: 0 35px;
		margin: 0 20px 0 0;
		outline: none;
		background: #BBB09B;
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
	.add-update-preview .closeBtn:hover {
		opacity: 0.5;
		.icon {
			color: rgba(64, 158, 255, 0.5);
		}
		.text {
			color: #fff;
		}
	}
</style>
