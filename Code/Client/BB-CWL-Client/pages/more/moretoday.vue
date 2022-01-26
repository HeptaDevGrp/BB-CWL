<template>
	<view class="base">
		<scroll-view scroll-y style="height: 1600rpx;width: 100%;" @scrolltolower="reachBottom">
			More Today Announcement
			<view @click="goBack()">
				Back
			</view>
			<view class="annoucementinfo">
				<view v-for="(item,index) in TodayShowList" :key="index" @click="AnnouncementClick(item)">
					<view>{{item["Title"]}}</view>
					<view>{{item["Posted On"]}}</view>
				</view>
			</view>
		</scroll-view>
	</view>
</template>

<script>
	import json from '../../../../Node/client_helper/import_data.js';
	export default {
		data() {
			return {
				TodayShowList:[]
			}
		},
		onLoad(item){
			let obj=item.itemlist.replace("\"([^\"]*)\"", "$1");
			this.TodayShowList=JSON.parse(obj)
			let data=json.data;
		},
		methods: {
			AnnouncementClick(item){
				let items=encodeURIComponent(JSON.stringify(item));
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

</style>
