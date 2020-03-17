<template>
    <div class="content">
    <h1>可能是最适合当代人使用的书签网页</h1>
    <ul 
    v-for="(folder,index) in folders"
    v-bind:key="index"
    >
    <h2>{{folder.title}}</h2>
    <div class="book_list">
        <li 
        v-for="(bookmark,cindex) in (folder.children)"
        v-bind:key="cindex"
        
        ><img @click="jump(bookmark.title,bookmark.href,bookmark._id.$oid,index,cindex)" :src="'https://www.80shihua.com/favicon.ico'"  class="logo"><a :href="bookmark.href" target="_blank" class="text">{{ bookmark.title }}</a></li>
        </div>
    </ul>
    </div>
</template>

<script>
export default {
    name : "BookMarks",
    props:{
        folders:Array
    },
    data:function(){
        return{
            title:'',
            href:'',
            id:''
        }
    },
    methods:{
        jump:function(title,href,id,pindex,cindex){
            //index数组索引值
            this.$emit("jump",true,title,href,id,pindex,cindex)
            //e.currentTarget.nextElementSibling.click();
        }
    }
}
</script>

<style scoped>
.logo{
    width: 32px;
    height: 32px;
    border-radius: 50%;
}
.text{
    text-align: center;
    position: absolute;
    margin-top: 40px;
    margin-left: -65px;
    width:100px;
    height:20px;
    text-decoration: none;
    color:darkcyan;
    overflow: hidden;
}
</style>