<template>
	<view class="settings">
		<view class="Back" @click="goBack()"></view>
		<view class="underline"></view>
		<view class="security"></view>
		<view class="profile"></view>
		<view class="Account">Account</view>
		<view class="Setting">Setting</view>
		<view class="USER1234">USER1234</view>
		<view class="profile_photo"></view>
		<view class="Logout">Logout</view>
		<view class="box"></view>
		<view class="top"></view>
		<view class="middle"></view>
		<view class="top2"></view>
		<view class="_1"></view>
		<view class="_2"></view>
		<view class="_3"></view>
		<view class="bottom"></view>
		<view class="background"></view>
	</view>
</template>
<script>
	import json from '../../../../Node/client_helper/import_data.js';
	export default {
		methods: {
			goBack(){
				uni.navigateBack({
					delta: 1
				})
			}
		}
	}
</script>
<style>
	@import "/pages/my/Settings/settings.css";
</style>