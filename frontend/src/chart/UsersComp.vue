<template>
    <div>
        <el-table :data="tableData" stripe style="width: 100%">
            <el-table-column prop="user_id" label="客户编号" width="50">
            </el-table-column>
            <el-table-column prop="username" label="客户姓名" width="300">
            </el-table-column>
            <el-table-column prop="email" label="邮箱">
            </el-table-column>
            <el-table-column prop="address" label="地址">
            </el-table-column>
        </el-table>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'LoginCanp',
    data() {
        return {
            tableData: []
        }
    },
    methods: {
        getData() {
            axios.get('http://localhost:8000/show/users/').then(
                response => {
                    console.log('请求成功', response.data)
                    if (response.data.code === 1) {
                        this.tableData = response.data.data
                    }
                    else {
                        this.$message.error('获取表单失败');
                    }
                },
                error => {
                    console.log('请求失败', error.message)
                    this.$message.error('请求失败');
                }
            )
        },
    },
    mounted() {
        this.getData();
    }
}
</script>

<style></style>
