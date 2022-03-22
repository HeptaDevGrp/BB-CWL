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
	</view>
</template>

<script>
	import json from '../../../../Node/client_helper/import_data.js';
	export default {
		methods: {
			my2set(){
				console.log('1');
				uni.navigateTo({
					url: './Settings/settings',
				})
			}
		}
	}
</script>

<style>
	@import "/pages/my/my.css";
</style>