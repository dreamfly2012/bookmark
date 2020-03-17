import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import Antd from 'ant-design-vue'
import 'ant-design-vue/dist/antd.css'
Vue.use(Antd)

Vue.config.productionTip = false
Vue.prototype.$http = axios

axios.defaults.baseURL = 'http://127.0.0.1:8888';


new Vue({
  render: h => h(App),
}).$mount('#app')
