// 该文件专门用于创建整个应用的路由器
import VueRouter from 'vue-router'
//引入组件
import showComp from '@/components/showComp.vue'
import LoginComp from '@/components/LoginComp.vue'

import OrdersComp from '@/chart/OrdersComp.vue'
import PaymentsComp from '@/chart/PaymentsComp.vue'
import BooksComp from '@/chart/BooksComp.vue'
import UsersComp from '@/chart/UsersComp.vue'
import ShoppingcartComp from '@/chart/ShoppingcartComp.vue'
import blankComp from '@/chart/blankComp.vue'
import SelectOrder from '@/chart/SelectOrder.vue'


//创建并暴露一个路由器
export default new VueRouter({
    routes: [
        {
            name: 'show',
            path: '/show',
            component: showComp,
            children: [
                {
                    name:'selectorder',
                    path:'selectorder',
                    component:SelectOrder
                },
                {
                    name:'blank',
                    path:'blank',
                    component: blankComp
                },
                {
                    name:'chart1',
                    path: 'books',
                    component: BooksComp,
                },
                {
                    name:'chart2',
                    path: 'users',
                    component: UsersComp,
                },
                {
                    name:'chart3',
                    path: 'orders',
                    component: OrdersComp,
                },
                {
                    name:'chart4',
                    path: 'payments',
                    component: PaymentsComp,
                },
                {
                    name:'chart5',
                    path: 'shoppingcart',
                    component: ShoppingcartComp,
                }
            ]
        },
        {
            name: 'login',
            path: '/login',
            component: LoginComp
        }
    ]
})
