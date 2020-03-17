<ul 
    v-for="(folder,index) in folders"
    v-bind:key="index"
    >
    <h2>test</h2>
    <div class="book_list">
        <li 
        v-for="(bookmark,cindex) in (folders[index])"
        v-bind:key="cindex"
        ><img :src="bookmark.logo||'https://www.80shihua.com/favicon.ico'"  class="logo"><a :href="bookmark.href" class="text">{{ bookmark.title }}</a></li>
        </div>
    </ul>