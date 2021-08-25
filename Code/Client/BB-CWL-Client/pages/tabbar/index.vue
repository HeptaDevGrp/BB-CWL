<template>
	<view class="base">
		<scroll-view scroll-y style="height: 1600rpx;width: 100%;" @scrolltolower="reachBottom">
			<view class="back">
				
			</view>
		    <view class="announcementstatic">
				<view class="announcementedge"></view>
				<view class="announcementco1"></view>
				<view class="announcementco2"></view>
				<view class="announcementcotext">Announcement</view>
				<view class="announcementbubble"></view>
				<view @click="MoreAnnouncementClick()" class="announcementmorebutton">More...</view>
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
			<view class="todaystatic">
				<view class="today">Today</view>
				<view class="todaylogo"></view>
				<view class="todaybubble"></view>
				<view @click="MoreTodayClick()" class="todaymorebutton">More...</view>
			</view>
			<view class="tomorrowstatic">
			    <view class="tomorrow">Tomorrow</view>
				<view class="tomorrowlogo"></view>
			    <view class="tomorrowbubble"></view>
			    <view @click="MoreTomorrowClick()" class="tomorrowmorebutton">More...</view>
			</view>
			<view class="futurestatic">
				<view class="future">Future</view>
				<view class="futurelogo"></view>
				<view class="futurebubble"></view>
				<view @click="MoreFutureClick()" class="futuremorebutton">More...</view>
			</view>
			<view class="todo">
				<view class="todaytodo"></view>
				<view class="tomorrowtodo"></view>
				<view class="futuretodo"></view>
			</view>
			<view class="clock">
			    <view>{{a}} {{b}}</view>
			</view>
			<view class="announcementinfo">
				<view @click="AnnouncementClick(0)" class="announcementinfo1">
					<view>{{AnnouncementShowList[0]["Title"]}}</view>
					<view>{{AnnouncementShowList[0]["Posted On"]}}</view>
				</view>
				<view @click="AnnouncementClick(1)" class="announcementinfo2">
					{{AnnouncementShowList[1]["Title"]}}
					<view>{{AnnouncementShowList[1]["Posted On"]}}</view>
				</view>
				<view @click="AnnouncementClick(2)" class="announcementinfo3">
					{{AnnouncementShowList[2]["Title"]}}
					<view>{{AnnouncementShowList[2]["Posted On"]}}</view>
				</view>
				<view @click="AnnouncementClick(3)" class="announcementinfo4">
					{{AnnouncementShowList[3]["Title"]}}
					<view>{{AnnouncementShowList[3]["Posted On"]}}</view>
				</view>
			</view>
		</scroll-view>
	</view>
</template>

<script>
	import json from '../../../../Node/client_helper/import_data.js';
	export default {
		data() {
			return {
				a:'',
				b:'',
				new_announcements_count:10,
				AnnouncementShowList:[],
				TodayShowList:[],
				TomorrowShowList:[],
				FutureShowList:[]
			}
		},
		created(){
			this.setTime()
			this.setDate()
		},
		onLoad() {
			let data=json.data;
			this.datascreening();
		},
		methods: {
			datascreening: function(){
				var num_an=json.data[0]["Posted By"]["length"]
				if(num_an>4){
					num_an=4
				}
				var announcement;
				for(var i=0;i<num_an;i++){
					announcement={
						"Posted By":json.data[0]["Posted By"][i],
						"Posted On":json.data[0]["Posted On"][i],
						"Posted To":json.data[0]["Posted To"][i],
						"Stipulate":json.data[0]["Stipulate"][i],
						"Title":json.data[0]["Title"][i]
						};
					this.AnnouncementShowList.push(announcement);
				}
				console.log(this.AnnouncementShowList)
			},
			setDate(){
				var date=new Date()
				var year=date.getFullYear();
				var month=date.getMonth()+1;
				var day=date.getUTCDate();
				var datepage=year+"/"+month+"/"+day
				this.a=datepage
				this.goTime()
			},
			setTime(){
				var time=new Date()
				var hours=time.getHours()
				var minute=time.getMinutes()
				var second=time.getSeconds()
				var daytime;
				if(minute==0){
					daytime=hours+":"+'00'
				}
				if(minute>0&&minute<10){
					daytime=hours+":"+'0'+minute
				}
				if(minute>=10){
					daytime=hours+":"+minute
				}
				if(second==0){
					daytime=daytime+":"+'00'
				}
				if(second>0&&second<10){
					daytime=daytime+":"+'0'+second
				}
				if(second>=10){
					daytime=daytime+":"+second
				}
				this.b=daytime
				this.goTime()
			},
			goTime(){
				setInterval(()=>{
					this.setDate()
					this.setTime()
				},1000)
			},
			AnnouncementClick(AncNum){
				uni.navigateTo({
					url: '../announcement/announcement?id='+AncNum.toString()
				})
			},
			MoreTodayClick(){
				uni.navigateTo({
					url: '../more/moretoday'
				})
			},
			MoreTomorrowClick(){
				uni.navigateTo({
					url: '../more/moretomorrow'
				})
			},
			MoreFutureClick(){
				uni.navigateTo({
					url: '../more/morefuture'
				})
			},
			MoreAnnouncementClick(){
				uni.navigateTo({
					url: '../more/moreannouncement'
				})
			}
		}
	}
</script>

<style>
@import "/pages/tabbar/index.css";

</style>
