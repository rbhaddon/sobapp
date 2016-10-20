using System.Collections;
using System.Collections.Generic;
using System;

namespace HexCrawlConstants {

	public static class TownData
	{
		public const int MAX_LOCATIONS = 8;
		public const int MAX_BUILTINS = 2;

		public static System.Random random = new System.Random();

		// Default world town names
		public static Dictionary<int, string> Names = new Dictionary<int, string>()
		{
			{1, "Brimstone"},
			{2, "Masthead"},
			{3, "Fort Burk"},
			{4, "West Witold"},
			{5, "Hill Town"},
			{6, "Serafin"},
			{7, "Fringe"},
			{8, "Wood's End"},
			{9, "Larberg's Landing"},
			{10, "Stone's Crossing"},
			{11, "Lestina"},
			{12, "Last Chance"},
			{13, "Fort Lopez"},
			{14, "Adlerville"},
			{15, "Flamme's Folly"},
			{16, "Fort Landy"},
			{17, "Conradt's Claim"},
			{18, "Wilshin's Lodge"},
			{19, "Seto's Mill"},
			{20, "San Miguel Mission"},
		};

		public static Dictionary<int, string> Types = new Dictionary<int, string>()
		{
			{2, "Town Ruins"},
			{3, "Haunted Town"},
			{4, "Plague Town"},
			{5, "Rail Town"},
			{6, "Standard Frontier Town"},
			{7, "Standard Frontier Town"},
			{8, "Standard Frontier Town"},
			{9, "Mining Town"},
			{10, "River Town"},
			{11, "Mutant Town"},
			{12, "Outlaw Town"},
		};

		public static Dictionary<int, string> GeographicTypes = new Dictionary<int, string>()
		{
			{5, "Rail Town"},
			{10, "River Town"},
		};

		public enum Status {Okay, Destroyed};

		public enum JobState {Started, Not_Started, Passed, Failed};

		public enum Trait {None, Trait1, Trait2, Trait3};

		public enum BuiltInType {Campsite, Hotel};

		public enum LocationType {
			GeneralStore, FrontierOutpost, Church, DocsOffice, Saloon, Blacksmith, SheriffsOffice,
			GamblingHall, StreetMarket, SmugglersDen, MutantQuarter, IndianTradingPost 
		};

		//}

		public static string[] LocationTypeName = {
			"General Store",
			"Frontier Outpost",
			"Church",
			"Doc's Office",
			"Saloon",
			"Blacksmith",
			"Sheriff's Office",
			"Gambling Hall",
			"Street Market",
			"Smuggler's Den",
			"Mutant Quarter",
			"Indian Trading Post"
		};

		public static string LocationToString(LocationType location)
		{
			return LocationTypeName [(int)location];
		}

	}
}
