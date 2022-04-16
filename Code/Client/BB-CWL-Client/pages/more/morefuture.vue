<template>
	<view class="base">
		<scroll-view scroll-y style="height: 1600rpx;width: 100%;" @scrolltolower="reachBottom">
			<view class="moreannouncement">
				<!-- 标题栏 -->
				<view class="矩形_8_拷贝"></view>
				<view class="矩形_8"></view>
				<view class="标题栏_拷贝_2"></view>
				<view class="Announcements">More Future</view>
				<!-- 三角形 -->
				<view class="形状_1_拷贝_2"></view>
				<view class="形状_1_拷贝"></view>
				<view class="形状_1"></view> 
				<!-- 背景 -->
				<view class="图层_3_拷贝"></view>
				<!-- Back 按钮-->
				<view class="back"></view>
				<view class="back_text" @click="goBack()">Back</view>
				<!-- 查找日期 查找课程-->
				<view class="fcourse"></view>
				<view class="fdate"></view>
			    <view class="nav-list">
			    	<view class="nav-li"
			    		 @click="MoreAnnouncementClick(index)"
			    		  v-for="(item,index) in FutureShowList" :key="index">
			    		<view class="rectangle_8">
			    			<view :class="[{'rectangle_91':index%2==0,
			    							'rectangle_92':index%2==1}]"></view>
			    		</view>
			    		 <view class="nav-title">{{FutureShowList[index]["Title"]}}</view>
			    	</view>
			    </view>
			</view>
		</scroll-view>
	</view>
</template>

<script>
	import json from 'database/client_helper/import_data.js';
	export default {
		data() {
			return {
				FutureShowList:[]
			}
		},
		onLoad(item){
			let obj=item.itemlist.replace("\"([^\"]*)\"", "$1");
			this.FutureShowList=JSON.parse(obj)
			let data=json.data;
		},
		methods: {
			MoreAnnouncementClick(item1){
				var items;
				console.log(item1)
				items=encodeURIComponent(JSON.stringify(this.FutureShowList[item1]));
				uni.navigateTo({
					url: '../announcement/announcement?itemlist='+items,
				})
			},
			goBack(){
				uni.navigateBack({
					delta: 1
				})
			}
		}
	}
</script>

<style>
    @import "/pages/more/moreannouncement.css";
	@import "/pages/more/moreancm.css";
</style>
