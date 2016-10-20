using UnityEngine;
using System.Collections;
using System;
using System.Linq;
using System.Security.Cryptography;

public static class Roll
{	
	/*
	public static int RollDice(System.Random rnd, int num)
	{
		//System.Random rnd = new System.Random ();
		return rnd.Next (1, num);
	}
	*/
	//public const int d6 = 6;

	public static int RollDice(int NumSides)
	{
		// Create a byte array to hold the random value.
		byte[] randomNumber = new byte[1];

		// Create a new instance of the RNGCryptoServiceProvider. 
		RNGCryptoServiceProvider Gen = new RNGCryptoServiceProvider();

		// Fill the array with a random value.
		Gen.GetBytes(randomNumber);

		// Convert the byte to an integer value to make the modulus operation easier.
		int rand = Convert.ToInt32(randomNumber[0]);

		// Return the random number mod the number
		// of sides.  The possible values are zero-
		// based, so we add one.

		return rand % NumSides + 1;
	}

	// Return a string because these values will be matched against JSON keys (which must be string)
	public static int D36()
	{
		return RollDice(6) * 10 + RollDice(6);
	}

	public static int D3()
	{
		return RollDice (3);
	}

	public static int D6()
	{
		return RollDice (6);
	}

	public static int D8()
	{
		return RollDice (8);
	}

	public static int D10()
	{
		return RollDice (10);
	}

	public static int D12()
	{
		return RollDice (12);
	}

	public static int D20()
	{
		return RollDice (20);
	}
}