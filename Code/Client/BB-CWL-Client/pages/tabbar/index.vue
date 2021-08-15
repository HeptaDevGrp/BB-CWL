
<template>
	<view class="base">
		<scroll-view scroll-y style="height: 1600rpx;width: 100%;" @scrolltolower="reachBottom">
			<view class="back">
		
			</view>
			<view class="announcementstatic">
				<view class="announcementedge"></view>
				<view class="announcementco1"></view>
				<view class="announcementco2"></view>
				<view class="announcementcotext">Announcements</view>
				<view class="announcementbubble"></view>
				<view class="announcementmorebutton">More...</view>
			</view>
			<view class="updatebutton">
				<view class="clockicon">
					<view class="clockco1"></view>
					<view class="clockco2"></view>
					<view class="clockco3"></view>
					<view class="clockco4"></view>
				</view>
			</view>
			<view class="calendarbutton">
				<view class="calendaricon">
					<view class="calendarco1"></view>
					<view class="calendarco2"></view>
					<view class="calendarco3"></view>
					<view class="calendarco4"></view>
					<view class="calendarco5"></view>
					<view class="calendarco6"></view>
					<view class="calendarco7"></view>
					<view class="calendarco8"></view>
					<view class="calendarco9"></view>
					<view class="calendarco10"></view>
				</view>
			</view>
			<view class="today">Today</view>
			<view class="tomorrow">Tomorrow</view>
			<view class="future">Future</view>
			<view class="todaylogo"></view>
			<view class="tomorrowlogo"></view>
			<view class="futurelogo"></view>
			<view class="todo">
				<view class="todaytodo"></view>
				<view class="tomorrowtodo"></view>
				<view class="futuretodo"></view>
			</view>
		</scroll-view>	
		<view class="bottom">
			
		</view>
	</view>		

</template>

<script>
	import json from '../../../../Node/client_helper/import_data.js';
	export default {
		data() {
			return {
				new_announcements_count:10,
				AnnouncementShowList:[],
				TodayShowList:[],
				TomorrowShowList:[],
				FutureShowList:[]
			}
		},
		onLoad() {
			let data=json.data;
		},
		methods: {

		}
	}
</script>

<style>
@import "/pages/tabbar/index.css";

</style>
