
<template>
	<view class="base">
		<scroll-view scroll-y style="height: 1500rpx;width: 100%;" @scrolltolower="reachBottom">
			<view class="back">
		
			</view>
			<view class="announcementstatic">
				<view class="announcementedge"></view>
				<view class="announcementco1"></view>
				<view class="announcementco2"></view>
				<view class="announcementcotext">Announcements</view>
			</view>
			<view class="clockbutton">
			
			</view>
			<view class="calendarbutton">

			</view>
			<view class="today">Today</view>
			<view class="tomorrow">Tomorrow</view>
			<view class="future">Future</view>
			<view class="todaylogo"></view>
			<view class="tomorrowlogo"></view>
			<view class="futurelogo"></view>
		
		</scroll-view>	
		<view class="bottom">
			
		</view>
	</view>		

</template>

<script>
	export default {
		data() {
			return {
				
			}
		},
		onLoad() {

		},
		methods: {

		}
	}
</script>

<style>
@import "/pages/tabbar/index.css";

</style>
