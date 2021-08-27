<template>
	<view class="base">
		<scroll-view scroll-y style="height: 1600rpx;width: 100%;" @scrolltolower="reachBottom">
			More Announcement
			<view @click="goBack()">
				Back
			</view>
			<view class="annoucementinfo">
				<view v-for="(item,index) in AnnouncementShowList" :key="index" @click="AnnouncementClick(index)">
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
				AnnouncementShowList:[]
			}
		},
		onLoad(){
			let data=json.data;
			this.datascreening();
		},
		methods: {
			datascreening: function(){
				var num_an=json.data[0]["Posted By"]["length"]
				var announcement;
				for(var i=0;i<num_an;i++){
					announcement={
						"Posted By":json.data[0]["Posted By"][i],
						"Posted On":json.data[0]["Posted On"][i],
						"Posted To":json.data[0]["Posted To"][i],
						"Stipulate":json.data[0]["Stipulate"][i],
						"Title":json.data[0]["Title"][i]
						};
					this.AnnouncementShowList.push(announcement);
				}
				console.log(this.AnnouncementShowList)
			},
			AnnouncementClick(AncNum){
				uni.navigateTo({
					url: '../announcement/announcement?id='+AncNum.toString()
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
