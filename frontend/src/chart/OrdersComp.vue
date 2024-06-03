<template>
    <div>
        <el-table :data="tableData" stripe style="width: 100%">
            <el-table-column prop="order_id" label="订单编号" width="50">
            </el-table-column>
            <el-table-column prop="book_id_id" label="图书编号">
            </el-table-column>
            <el-table-column prop="user_id_id" label="客户编号">
            </el-table-column>
            <el-table-column prop="quantity" label="数量">
            </el-table-column>
            <el-table-column prop="total_price" label="总价">
            </el-table-column>
            <el-table-column prop="date" label="日期">
            </el-table-column>
            <el-table-column label="操作">
                <template slot-scope="scope">
                    <el-button @click="deleterow(scope.row.order_id.toString())" type="danger"
                        size="mini">删除</el-button>
                    <el-button @click="changeorder(scope.row.order_id.toString())" type="warning" size="mini">更改</el-button>
                </template>
            </el-table-column>
        </el-table>

        <!-- 添加 el-drawer 组件 -->
        <el-drawer title="订单详情" :visible.sync="editdrawerVisible" direction="rtl" :with-header="true" size="30%">
            <!-- 这里放入抽屉内容 -->
            <div class="demo-drawer__content" style="padding-left: 10%; padding-right: 10%">
                <el-form>
                    <el-form-item label="更新数量">
                        <el-input v-model="editform.new_number" autocomplete="off"></el-input>
                    </el-form-item>
                </el-form>
                <div class="demo-drawer__footer">
                    <el-button @click="editSubmit">提交</el-button>
                </div>
            </div>
        </el-drawer>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'LoginCanp',
    data() {
        return {
            tableData: [],
            editdrawerVisible: false,

            editform: {
                new_number: '',
                order_id:''
            },
        }
    },
    methods: {
        getData() {
            axios.get('http://localhost:8000/show/orders/').then(
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

        deleterow(id) {
            console.log('即将删除订单' + id)
            axios.post('http://localhost:8000/change/deleteorder/', {
                order_id: id
            }).then(
                response => {
                    console.log('请求成功', response.data)
                    if (response.data.code === 1) {
                        this.$message({
                            message: '删除订单成功！',
                            type: 'success'
                        });
                        this.$emit('call-parent-method');
                    }
                    else {
                        this.$message.error('删除订单失败！');
                    }
                },
                error => {
                    console.log('请求失败', error.message)
                    this.$message.error('请求失败');
                }
            )
        },
        changeorder(id){
            this.editdrawerVisible = true,
            this.editform.order_id = id
        },
        editSubmit() {
            axios.post('http://localhost:8000/change/changeorder/', {
                number: this.editform.new_number,
                order_id: this.editform.order_id
            }).then(
                response => {
                    console.log('请求成功', response.data)
                    if (response.data.code === 1) {
                        this.$message({
                            message: '更改订单成功！',
                            type: 'success'
                        });
                        this.$emit('call-parent-method');
                    }
                    else {
                        this.$message.error('更改订单失败！');
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
