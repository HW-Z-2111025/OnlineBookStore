<template>
    <div>
        <el-table :data="tableData" stripe style="width: 100%">
            <el-table-column prop="order_id" label="订单编号" width="50">
            </el-table-column>
            <el-table-column prop="title" label="书名">
            </el-table-column>
            <el-table-column prop="quantity" label="数量">
            </el-table-column>
            <el-table-column prop="total_price" label="总价">
            </el-table-column>
            <el-table-column prop="order_date" label="订单日期">
            </el-table-column>
            <el-table-column prop="username" label="客户姓名">
            </el-table-column>
        </el-table>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'SelectOrder',
    data() {
        return {
            tableData: [],
            editdrawerVisible: false,

            editform: {
                new_number: '',
                order_id: ''
            },

            orderId: this.$route.params.order_id
        }
    },
    methods: {
        getData() {
            console.log('收集到的order-ID'+this.orderId)
            if (this.orderId) {
                axios.post('http://localhost:8000/query/infoorder/', {
                    order_id: this.orderId
                }).then(
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
            }
        },
    },
    mounted() {
        this.getData();
    }
}
</script>

<style></style>
