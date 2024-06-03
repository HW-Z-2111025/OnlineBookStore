<template>
    <div id='Login'>
        <el-card class="box-card">
            <div slot="header" class="clearfix">
                <span>登录</span>
            </div>
            <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="100px"
                class="demo-ruleForm">
                <el-form-item label="账号" prop="account">
                    <el-input v-model="ruleForm.account" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="密码" prop="pass">
                    <el-input type="password" v-model="ruleForm.pass" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item class="full-width">
                    <el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>
                    <el-button @click="resetForm('ruleForm')">重置</el-button>
                </el-form-item>
            </el-form>
        </el-card>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'LoginCanp',
    data() {
        var validateAccount = (rule, value, callback) => {
            if (value === '') {
                callback(new Error('请输入账号'));
            } else {
                callback();
            }
        };
        var validatePass = (rule, value, callback) => {
            if (value === '') {
                callback(new Error('请输入密码'));
            } else {
                callback();
            }
        };
        return {
            ruleForm: {
                account: '',
                pass: ''
            },
            rules: {
                account: [
                    { validator: validateAccount, trigger: 'blur' }
                ],
                pass: [
                    { validator: validatePass, trigger: 'blur' }
                ]
            }
        };
    },
    methods: {
        submitForm(formName) {
            this.$refs[formName].validate((valid) => {
                if (valid) {
                    // 向后端提交！
                    axios.post('http://localhost:8000/login/', {
                        username: this.ruleForm.account,
                        password: this.ruleForm.pass
                    }).then(
                        response => {
                            console.log('请求成功', response.data)
                            if (response.data.data === 1) {
                                this.$message({
                                    message: '登陆成功',
                                    type: 'success'
                                });
                                this.$emit('call-parent-method');
                            }
                            else{
                                this.$message.error('账号或密码错误');
                            }
                        },
                        error => {
                            console.log('请求失败', error.message)
                            this.$message.error('请求失败');
                        }
                    )
                } else {
                    console.log('error submit!!');
                    return false;
                }
            });
        },
        resetForm(formName) {
            this.$refs[formName].resetFields();
        }
    }
}
</script>

<style>
.text {
    font-size: 14px;
}

.item {
    margin-bottom: 18px;
}

.clearfix:before,
.clearfix:after {
    display: table;
    content: "";
}

.clearfix:after {
    clear: both
}

.box-card {
    width: 40%;
    margin-left: 30%;
    margin-right: 30%;
    margin-top: 20px;
}

.full-width {
    width: 100%;
    margin-bottom: 20px;
}
</style>
