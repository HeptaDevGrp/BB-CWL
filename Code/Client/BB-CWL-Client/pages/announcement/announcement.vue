<template>
	<view class="base">
		<scroll-view scroll-y style="height: 1600rpx;width: 100%;" @scrolltolower="reachBottom">
			<meta charset="utf-8">
			<view class="learn_more">
				<!-- /*求是鹰图标*/ -->
				<view class="group_11">              
					<view class="layer_12"></view>
					<view class="oval_2"></view>
				</view>
				<!-- /*背景*/ -->
				<view class="title_bar"></view>
				<view class="layer_3"></view>
				<view class="shape_3"></view>
				<view class="rounded_rectangle_5"></view>
				<view class="background"></view>
				<!-- /*announcements图标*/ -->
				<view class="rectangle_5"></view>
				<view class="rectangle_4"></view>
				<view class="Announcements">Announcements</view>
				<!-- /*下方导航栏*/ -->
				<view class="group_10">             
					<view class="layer_11"></view>
					<view class="layer_10"></view>
					<view class="layer_9"></view>
					<view class="navigation_bar"></view>
				</view>
				<view class="back"></view>
				<view class="back_text" @click="goBack()">Back</view>
			</view>
			<view class="ancmstatic">
				<view style="white-space: pre-wrap" charset="gbk" class="a_title">
					<view>{{annoucement["Title"]}}</view>
					<view>{{'\n'}}</view>
					<view>{{annoucement["Posted By"]}}</view>
					<view>{{'\n'}}</view>
					<view>{{annoucement["Posted On"]}}</view>
					<view>{{'\n'}}</view>
					<view>{{annoucement["Posted To"]}}</view>
					<view>{{'\n'}}</view>
					<view>{{annoucement["Stipulate"]}}</view>
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
				new_announcements_count:10,
				annoucement:{}
			}
		},
		onLoad(item){
			let obj=item.itemlist.replace("\"([^\"]*)\"", "$1");
			this.annoucement=JSON.parse(obj)
			let data=json.data;
		},
		methods: {
			datascreening(AncNum){
				var announcement;
				console.log(AncNum)
				announcement={
					"Posted By":json.data[0]["Posted By"][AncNum],
					"Posted On":json.data[0]["Posted On"][AncNum],
					"Posted To":json.data[0]["Posted To"][AncNum],
					"Stipulate":json.data[0]["Stipulate"][AncNum],
					"Title":json.data[0]["Title"][AncNum]
					};
				this.AnnouncementShowList.push(announcement)
				console.log(announcement)
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
@import "/pages/announcement/announcement.css";
</style>
