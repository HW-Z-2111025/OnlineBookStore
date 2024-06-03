<template>
    <div id='show'>
        <el-container style="height: 950px">
            <el-aside width="200px">
                <el-col>
                    <el-menu class="el-menu-vertical-demo" @select="handleSelect" default-active='1'>
                        <el-menu-item index="1">
                            <i class="el-icon-reading"></i>
                            <span slot="title">书</span>
                        </el-menu-item>
                        <el-menu-item index="2">
                            <i class="el-icon-user"></i>
                            <span slot="title">用户</span>
                        </el-menu-item>
                        <el-menu-item index="3">
                            <i class="el-icon-tickets"></i>
                            <span slot="title">订单</span>
                        </el-menu-item>
                        <el-menu-item index="4">
                            <i class="el-icon-money"></i>
                            <span slot="title">支付记录</span>
                        </el-menu-item>
                        <el-menu-item index="5">
                            <i class="el-icon-shopping-cart-2"></i>
                            <span slot="title">购物车</span>
                        </el-menu-item>
                    </el-menu>
                </el-col>
            </el-aside>

            <el-container id="show-container">
                <el-header id="chart-header">
                    <el-dropdown>
                        <el-button type="primary" icon="el-icon-plus" circle></el-button>
                        <el-dropdown-menu slot="dropdown">
                            <el-dropdown-item>
                                <el-button type="text" @click="addOrder" style="color: black;">增加订单</el-button>
                            </el-dropdown-item>
                        </el-dropdown-menu>
                    </el-dropdown>
                    <el-dropdown>
                        <el-button type="primary" icon="el-icon-search" circle style="margin-left: 10px;"></el-button>
                        <el-dropdown-menu slot="dropdown">
                            <el-dropdown-item>
                                <el-button type="text" @click="searchOrder" style="color: black;">查询订单</el-button>
                            </el-dropdown-item>
                        </el-dropdown-menu>
                    </el-dropdown>
                    <el-button type="serch" icon="el-icon-refresh-right" circle style="margin-left: 10px;"
                        @click="reloadPage"></el-button>
                </el-header>

                <el-main>
                    <router-view @call-parent-method="reloadPage"></router-view>
                </el-main>
            </el-container>

            <!-- 添加 el-drawer 组件 -->
            <el-drawer title="订单详情" :visible.sync="orderdrawerVisible" direction="rtl" :with-header="true" size="30%">
                <!-- 这里放入抽屉内容 -->
                <div class="demo-drawer__content" style="padding-left: 10%; padding-right: 10%">
                    <el-form>
                        <el-form-item label="客户编号">
                            <el-input v-model="orderform.user_id" autocomplete="off"></el-input>
                        </el-form-item>
                        <el-form-item label="图书编号">
                            <el-input v-model="orderform.book_id" autocomplete="off"></el-input>
                        </el-form-item>
                        <el-form-item label="数量">
                            <el-input v-model="orderform.num" autocomplete="off"></el-input>
                        </el-form-item>
                    </el-form>
                    <div class="demo-drawer__footer">
                        <el-button @click="addOrderSubmit">提交</el-button>
                    </div>
                </div>
            </el-drawer>
            <el-drawer title="查询订单" :visible.sync="userorderdrawerVisible" direction="rtl" :with-header="true" size="30%">
                <!-- 这里放入抽屉内容 -->
                <div class="demo-drawer__content" style="padding-left: 10%; padding-right: 10%">
                    <el-form>
                        <el-form-item label="订单编号">
                            <el-input v-model="userorder.order_id" autocomplete="off"></el-input>
                        </el-form-item>
                    </el-form>
                    <div class="demo-drawer__footer">
                        <el-button @click="searchOrderSubmit">提交</el-button>
                    </div>
                </div>
            </el-drawer>
        </el-container>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    name: 'showComp',
    data() {
        const item = {
            date: '2016-05-02',
            name: '王小虎',
            address: '上海市普陀区金沙江路 1518 弄'
        };
        return {
            addChartFormVisible: false,
            tableData: Array(20).fill(item),

            orderdrawerVisible: false, // 控制抽屉显示与隐藏的变量
            userorderdrawerVisible: false,

            curr_index: '1',

            //增加订单的变量
            orderform: {
                user_id: '',
                book_id: '',
                num: '',
            },

            //查询订单
            userorder: {
                order_id : ''
            }
        }
    },
    methods: {

        //控制显示界面
        handleSelect(index) {
            console.log('选择了' + index)
            this.$router.replace({ name: "chart" + index }, () => { }, () => { });
            this.curr_index = index
        },
        reloadPage() {
            console.log('reload')
            this.$router.replace({ name: 'blank' }, () => { }, () => { });
            setTimeout(() => {
                console.log('reload');
                this.handleSelect(this.curr_index);
            }, 100);
        },
        selectOrder() {
            this.$router.replace({ name: 'blank' }, () => { }, () => { });
            setTimeout(() => {
                console.log('reload');
                this.$router.replace({ name: "selectorder" , params: { order_id: this.userorder.order_id } }, () => { }, () => { });
            }, 100);
        },

        //添加订单
        addOrder() {
            console.log('开始添加')
            this.orderdrawerVisible = true
        },
        addOrderSubmit() {
            console.log(this.orderform)
            axios.post('http://localhost:8000/change/addorder/', {
                user_id: this.orderform.user_id,
                book_id: this.orderform.book_id,
                quantity: this.orderform.num
            }).then(
                response => {
                    console.log('请求成功', response.data)
                    if (response.data.code === 1) {
                        this.$message({
                            message: '订单添加成功！',
                            type: 'success'
                        });
                    }
                    else {
                        this.$message.error('添加失败');
                    }
                },
                error => {
                    console.log('请求失败', error.message)
                    this.$message.error('请求失败');
                }
            )

            this.user_id = ''
            this.book_id = ''
            this.num = ''
        },

        //查询订单
        searchOrder() {
            this.userorderdrawerVisible = true
        },
        searchOrderSubmit() {
            axios.post('http://localhost:8000/query/infoorder/', {
                order_id: this.userorder.order_id
            }).then(
                response => {
                    console.log('请求成功', response.data)
                    if (response.data.code === 1) {
                        this.$message({
                            message: '订单查询成功！',
                            type: 'success'
                        });
                        this.userorderdrawerVisible = false;
                        this.selectOrder();
                    }
                    else {
                        this.$message.error('订单查询失败');
                    }
                },
                error => {
                    console.log('请求失败', error.message)
                    this.$message.error('请求失败');
                }
            )
        }
    }
};
</script>

<style>
#chart-header {
    padding: 8px;
    text-align: center;
}
</style>
