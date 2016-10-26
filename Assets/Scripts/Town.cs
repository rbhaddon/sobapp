//using UnityEngine;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

using HexCrawlConstants;

[Serializable]
public class Town
{
	public string name;
	public TownData.Status status;
	public int size; // should be a property
	public int max_size;
	public int max_builtins;
	public string type;
	public TownTrait trait;
	public JobData[] jobs;
	public TownData.BuiltInType[] builtIns;
	public List<int> locations = new List<int>();
	public string[] keywords;

	public Town()
	{
		name = "";
		status = TownData.Status.Okay;
		size = Roll.D8 ();
		max_size = TownData.MAX_LOCATIONS;
		max_builtins = TownData.MAX_BUILTINS;
		type = GetTownType ();
		trait = new TownTrait ();
		jobs = new JobData [TownData.MAX_BUILTINS];
		builtIns = new TownData.BuiltInType[] {TownData.BuiltInType.Campsite, TownData.BuiltInType.Hotel};
//		for (int i = 0; i < size; i++) {
//			locations.Add(Roll.D12 ());
		//		}
		keywords = new string[]{ "Town" };
		SetLocations (size);
	}

	public static Town Create()
	{
		Town town = new Town ();
		town.type = TownData.Types [Roll.D6 () + Roll.D6 () - 2];
		town.size = Roll.D8 ();

		return town;
	}

	// Return any town type
	public static string GetTownType()
	{
		int roll2d6 = Roll.D6() + Roll.D6();
		return TownData.Types [roll2d6];
	}

	// Return town types other than Rail or River, since those are designated by the map
	public static string GetNonGeographicTownType()
	{
		string type = "";
		do {
			type = GetTownType();
		} while (TownData.GeographicTypes.ContainsValue(type));

		return type;
	}

	public void SetLocations(int num, params int[] fixedLocs)
	{
		List<int> responses = new List<int>();
		Dictionary<int, string> locations = new Dictionary<int, string>(TownData.Locations);

		foreach (int loc in fixedLocs)
		{
			responses.Add(loc);
			if (locations.ContainsKey (loc)) {
				locations.Remove (loc);
			}
		}

		if (fixedLocs.Length >= num)
		{
			this.locations = responses;
		}

		foreach (int pick in locations.Keys.OrderBy (x => TownData.random.Next ()).Take (num - fixedLocs.Length))
		{
			responses.Add (pick);
		}
		this.locations = responses;


	}
}

[Serializable]
public class JobData
{
	public int jobNumber;
	public int? timeRemaining = null;
	public string startLocation = "";
	public string turnInLocation = "";
	public TownData.JobState jobState;	
}