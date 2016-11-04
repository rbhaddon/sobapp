using UnityEngine;
using UnityEngine.UI;
//using System.Collections;
using HexCrawlConstants;

public class AilmentButtonOnClick : MonoBehaviour {

	public AilmentType ailment;
	public GameObject ailmentPanel;
	public Text chartTitleText;

	public void RollAilment()
	{
		//Debug.Log("Rolling for " + ailment);
		chartTitleText.text = ailment.ToString();
		foreach (Text text in ailmentPanel.GetComponentsInChildren<Text>())
		{
			switch (text.name)
			{
			case "AilmentNameText":
			case "AilmentRollText":
			case "AilmentFlavorText":
			case "AilmentEffectText":
				text.text = "";
				break;
			default:
				break;
			}
		}
		ailmentPanel.SetActive (true);
	}
}