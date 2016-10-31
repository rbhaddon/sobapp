using UnityEngine;
using System.Collections;
using HexCrawlConstants;

public class AilmentButtonOnClick : MonoBehaviour {

	public AilmentType ailment;

	// Use this for initialization
	void Start () {
	
	}

	public void RollAilment()
	{
		Debug.Log("Rolling for " + ailment);
	}
}
