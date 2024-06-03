<template>
    <div>
        <el-table :data="tableData" stripe style="width: 100%">
            <el-table-column prop="payment_id" label="支付记录id" width="80">
            </el-table-column>
            <el-table-column prop="order_id_id" label="订单遍号">
            </el-table-column>
            <el-table-column prop="payment_method" label="支付方式">
            </el-table-column>
            <el-table-column prop="payment_date" label="日期">
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
            axios.get('http://localhost:8000/show/payments/').then(
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
