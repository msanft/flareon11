using System;
using Org.BouncyCastle.Math;
using Org.BouncyCastle.Security;
using Org.BouncyCastle.Math.EC;
using Org.BouncyCastle.Utilities.Encoders;

class Program
{
    static void Main(string[] args)
    {
        InitializePrng();
    }

    static void InitializePrng()
    {
        BigInteger p = new BigInteger("c90102faa48f18b5eac1f76bb40a1b9fb0d841712bbe3e5576a7a56976c2baeca47809765283aa078583e1e65172a3fd", 16);
        Console.WriteLine($"Curve Prime: {p}");

        BigInteger a = BigInteger.Zero;
        BigInteger b = BigInteger.Zero;

        FpCurve curve = new FpCurve(p, a, b);

        BigInteger bigInt1 = new BigInteger("087b5fe3ae6dcfb0e074b40f6208c8f6de4f4f0679d6933796d3b9bd659704fb85452f041fff14cf0e9aa7e45544f9d8", 16);
        BigInteger bigInt2 = new BigInteger("127425c1d330ed537663e87459eaa1b1b53edfe305f6a79b184b3180033aab190eb9aa003e02e9dbf6d593c5e3b08182", 16);

        ECPoint point = curve.CreatePoint(bigInt1, bigInt2);
        Console.WriteLine($"Point: {point}");

        SecureRandom rand = new SecureRandom();
        Console.WriteLine($"BC Random: {rand}");

        System.Random sysrand = new System.Random();
        Console.WriteLine($"System Random: {sysrand}");

        return;
    }

    static void SomeXORCrypto() {
        BigInteger foo = newBigInteger("133713371337133713371337133713371337133713371337133713371337133713371337133713371337133713371337", 16);


    }
}
