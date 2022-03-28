<template>
	<view class="login page">
		<view class="log_in">
			<view class="login" @click="login_check()">
				<view class="Login">Login</view>
			</view>
			<view class="enter_password">
				<view class="Password">Password</view>
				<view class="underline"></view>
				<view class="blank"></view>
			</view>
			<view class="enter_userID">
				<view class="User_ID_">User ID</view>
				<view class="underline1"></view>
				<view class="blank1"></view>
			</view>
			<view class="profile_photo"></view>
			<view class="top"></view>
			<view class="middle"></view>
			<view class="top2"></view>
		</view>
		<view class="background-image"></view>
	</view>
</template>

<script>
	export default {
		methods: {
			login_check(){
				console.log(1);
				var psw_correct=1; // 密码是否正确，等待登录系统的接口
				if(psw_correct){
					uni.switchTab({
						url: '/pages/my/my',
					})
				}
			}
		}
	}
</script>

<style>
	@import "/pages/my/Login.css"
</style>