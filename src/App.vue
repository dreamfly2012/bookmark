<template>
  <div id="app">
    <BookMarks v-if="folders.length" :folders="folders" @jump="showstatus(arguments)"/>

    <a-modal
      :title="ModalText"
      :visible="visible"
      @ok="handleOk"
      :confirmLoading="confirmLoading"
      @cancel="handleCancel"
    >
    
        <a-form-item label="标题" :label-col="{ span: 5 }" :wrapper-col="{ span: 18 }">
          <a-input v-model="title_value" 
            
          />
        </a-form-item>

        <a-form-item label="链接" :label-col="{ span: 5 }" :wrapper-col="{ span: 18 }">
          <a-input v-model="url_value"
            
          />
        </a-form-item>
        
        <a-form-item :wrapper-col="{ span: 12, offset: 5 }">
          <a-button type="primary" @click="handleSubmit">
            修改
          </a-button>
          <input type="hidden" :value="id_value"/>
        </a-form-item>
      
    </a-modal>


  
  </div>

</template>

<script>
import BookMarks from './components/BookMarks.vue'

export default {
  name: 'App',
  components: {
    BookMarks
  },
  methods:{
     handleSyncInput(event){
        this.valueSync=event.target.value;
    },

    showstatus(param){
      this.visible = param[0]
      this.title_value = param[1]
      this.url_value = param[2]
      this.id_value = param[3]
      this.pindex = param[4]
      this.cindex = param[5]
    },
    handleCancel(){
      this.visible = false
    },
    handleOk(){
      this.visible = false
    },
    handleSubmit(){
      let pindex = this.pindex
      let cindex = this.cindex
      this.$set(this.folders[pindex]['children'][cindex], 'title', this.title_value)
      this.$set(this.folders[pindex]['children'][cindex], 'title', this.title_value)
      this.$set(this.folders[pindex]['children'][cindex], 'href', this.url_value)
      
      
      

      this.$http
      .get('/change',{params:{title:this.title_value,url:this.url_value,id:this.id_value}})
      .then(response => {
        
        console.log(response.data);
        
      })
      this.visible = false
    },
    open(){

    },
    close(){

    },
  },
  data:function(){
    return {
        folders:[
            // [{'title':'google','id':1},{'title':'zhihu','id':3},{'title':'zhihu','id':3},{'title':'zhihu','id':3},{'title':'zhihu','id':3},{'title':'zhihu','id':3},{'title':'zhihu','id':3},{'title':'zhihu','id':3},{'title':'zhihu','id':3},{'title':'zhihu','id':3},{'title':'zhihu','id':3},{'title':'zhihu','id':3},{'title':'zhihu','id':3},{'title':'zhihu','id':3},{'title':'zhihu','id':3},{'title':'zhihu','id':3},{'title':'zhihu','id':3},{'title':'zhihu','id':3},{'title':'zhihu','id':3},{'title':'zhihu','id':3},{'title':'zhihu','id':3},{'title':'zhihu','id':3}],
            // [{'title':"baidu",'id':4},{'title':'zhihu','id':3}],
            // [{'title':'douban','id':5}]
        ],
        ModalText: '编辑书签',
        visible: false,
        confirmLoading: false,
        show:false,
        title_value:'',
        url_value:'',
        id_value:'',
        pindex:'',
        cindex:'',
        form: this.$form.createForm(this),
    }
    
  },
  mounted (){
    
    this.$http
      .get('/')
      .then(response => {
        
        this.folders = response.data;
        
      })
  }

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

ul {
  list-style: none;
  overflow: hidden;
}

h2{
  padding-right:10px;
  display: inline;
  float:left;
  width:100px;
  border-right: 5px solid #248b24;
}

ul{
  min-height: 100px;
}


li{
   float:left;
   height: 75px;
  width:100px;
}
ul::after{
  clear: both;
}
.book_list{
  overflow: hidden;
}

</style>
