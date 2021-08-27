<template>
	<view class="base">
		<scroll-view scroll-y style="height: 1600rpx;width: 100%;" @scrolltolower="reachBottom">
			More Today Announcement
			<view @click="goBack()">
				Back
			</view>
		</scroll-view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				
			}
		},
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

</style>
