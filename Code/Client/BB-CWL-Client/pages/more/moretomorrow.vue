<template>
	<view class="base">
		<scroll-view scroll-y style="height: 1600rpx;width: 100%;" @scrolltolower="reachBottom">
			More Tomorrow Announcement
			<view @click="goBack()">
				Back
			</view>
			<view class="annoucementinfo">
				<view v-for="(item,index) in TomorrowShowList" :key="index" @click="TomorrowClick(item)">
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
				TomorrowShowList:[]
			}
		},
		onLoad(item){
			let obj=item.itemlist.replace("\"([^\"]*)\"", "$1");
			this.TomorrowShowList=JSON.parse(obj)
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
