<template>
	<view class="base">
		<scroll-view scroll-y style="height: 1600rpx;width: 100%;" @scrolltolower="reachBottom">
			Announcement
			<view @click="goBack()">
				Back
			</view>
			<view style="white-space: pre-wrap" charset="gbk">
				{{annoucement["Title"]}}
				{{'\n'}}
			</view>
			<view style="white-space: pre-wrap" charset="gbk">
				{{annoucement["Posted By"]}}
				{{'\n'}}
			</view>
			<view style="white-space: pre-wrap" charset="gbk">
				{{annoucement["Posted On"]}}
				{{'\n'}}
			</view>
			<view style="white-space: pre-wrap" charset="gbk">
				{{annoucement["Posted To"]}}
				{{'\n'}}
			</view>
			<view style="white-space: pre-wrap" charset="gbk">
				{{annoucement["Stipulate"]}}
				{{'\n'}}
			</view>
		</scroll-view>
	</view>
</template>

<script>
	import json from '../../../../Node/client_helper/import_data.js';
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

</style>
