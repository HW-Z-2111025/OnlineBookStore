<template>
    <div>
        <el-table :data="tableData" stripe style="width: 100%">
            <el-table-column prop="shopping_cart_id" label="购物车id" width="65">
            </el-table-column>
            <el-table-column prop="book_id_id" label="图书编号">
            </el-table-column>
            <el-table-column prop="user_id_id" label="客户编号">
            </el-table-column>
            <el-table-column prop="quantity" label="数量" width="300">
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
            axios.get('http://localhost:8000/show/shoppingcart/').then(
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
