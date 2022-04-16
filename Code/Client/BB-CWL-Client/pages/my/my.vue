<template>
	<view class="My">
		<view class="top"></view>
		<view class="top2"></view>
		<view class="middle">
			<view class="profile_photo"></view>
			<view class="USER1234">USER1234</view>
			<view class="useID123">useID123</view>
		</view>
		<view class="click">
			<view class="Message"></view>
			<view class="Setting" @click="my2set()"></view>
		</view>
		<view class="User_Guide"></view>
		<!-- <view class="guide">
			<view class="_1" @click="my2index()"></view>
			<view class="_2"></view>
			<view class="_3" @click="my2crs()"></view>
			<view class="bottom"></view>
		</view> -->
	</view>
</template>

<script>
	import json from 'database/client_helper/import_data.js';
	export default {
		onLoad() {
			this.login();
		},
		methods: {
			login(){
				uni.navigateTo({
					url: '/pages/my/Login',
				})
			},
			my2set(){
				uni.navigateTo({
					url: './Settings/settings',
				})
			},
			// my2index(){
			// 	console.log(1);
			// 	uni.switchTab({
			// 		url: '/pages/tabbar/index',
			// 	})
			// },
			// my2crs(){
			// 	console.log(2);
			// 	uni.switchTab({
			// 		url: '/pages/courses/courses',
			// 	})
			// }
		}
	}
</script>

<style>
	@import "/pages/my/my.css";
</style>