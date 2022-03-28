<template>
	<view class="edit_profile">
		<view class="Back" @click="goBack()"></view>
		<view class="Profile">Profile</view>
		<view class="profile_photo">
			<view class="Profile_Photo_">Profile Photo</view>
			<view class="profile_photo2"></view>
			<view class="box4"></view>
			<view class="top"></view>
			<view class="middle"></view>
			<view class="top2"></view>
		</view>
		<view class="Name">
			<view class="USER1234">User1234</view>
			<view class="box2"></view>
			<view class="Name_">Name</view>
			<view class="box3"></view>
		</view>
		<view class="User_ID">
			<view class="useID123_">userID123</view>
			<view class="box"></view>
			<view class="User_ID1">User ID</view>
			<view class="box1"></view>
		</view>
		<view class="background"></view>
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
	@import "/pages/my/Settings/setting_items/profile.css";
</style>
