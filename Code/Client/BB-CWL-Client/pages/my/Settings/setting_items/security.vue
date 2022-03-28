<template>
	<view class="edit_profile">
		<view class="Back" @click="goBack()"></view>
		<view class="Security">Security</view>
		<view class="top"></view>
		<view class="top2"></view>
		<view class="middle"></view>
		<view class="Password">
			<view class="password123">password123</view>
			<view class="box2"></view>
			<view class="Password_">Password</view>
			<view class="box3"></view>
		</view>
	</view>
</template>

<script>
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
	@import "/pages/my/Settings/setting_items/security.css";
</style>
