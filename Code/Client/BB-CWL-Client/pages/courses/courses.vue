<template>
	<scroll-view scroll-y style="height: 2400rpx;width: 100%;" @scrolltolower="reachBottom">
		<meta charset="utf-8">
		<view class="courses">
			<view class="courses_str">Courses</view>
			<view class="title_bar"></view>
			<view class="layer_3"></view>
			<view class="group_1">
				<view class="courses_str">Courses</view>
				<view class="rectangle_4"></view>
			</view>
			<view class="nav-list">
				<view class="nav-li"
					 @click="MoreAnnouncementClick(index)"
					  v-for="(item,index) in coursec" :key="index">
					<view class="rectangle_8">
						<view :class="[{'rectangle_91':index%2==0,
										'rectangle_92':index%2==1}]"></view>
					</view>
					 <view class="nav-title">{{coursec[index]}}</view>
				</view>
			</view>
		</view>
	</scroll-view>
</template>

<script>
	import json from '../../../../Node/client_helper/import_data_0.js';
	export default {
		data() {
			return {
				AnnouncementShowList:[],
				elements:{},
				coursec:[],
				total_cate:0
			}
		},
		onLoad() {
			let data=json.data;
			this.getcourses();
		},
		methods:{
			getcourses: function(){
				var num_an=json.data[0]["Posted To"]["length"];
				var ancm,ctgy;
				for(var i=0;i<num_an;i++){
					ancm={
						"Posted By":json.data[0]["Posted By"][i],
						"Posted On":json.data[0]["Posted On"][i],
						"Posted To":json.data[0]["Posted To"][i],
						"Stipulate":json.data[0]["Stipulate"][i],
						"Title":json.data[0]["Title"][i]
						};
					this.AnnouncementShowList.push(ancm);
					var incl=0;
					for(var key in this.elements){
						if(key==ancm["Posted To"]){
							incl=1;
							break;
						}
					}
					if(incl==0){
						this.total_cate++;
						this.coursec.push(ancm["Posted To"])
						this.elements[ancm["Posted To"]]=[ancm];
					} else{
						this.elements[ancm["Posted To"]].push(ancm);
					}
				}
			},
			MoreAnnouncementClick(item1){
				var items;
				console.log(item1)
				items=encodeURIComponent(JSON.stringify(this.elements[this.coursec[item1]]));
				uni.navigateTo({
					url: '../more/moreannouncement?itemlist='+items,
				})
			}
		}
	}
</script>

<style>
	@import "/pages/courses/course.css";
</style>
